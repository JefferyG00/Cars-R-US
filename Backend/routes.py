from flask import request, jsonify
from app import app, db
from models import Car, Dealership, Customer, Sale, ServiceAppointment, Cart, Review

@app.route('/')
def hello_world():
    return 'Hello, Cars-R-Us!'

@app.route('/dealerships', methods=['GET'])
def get_dealerships():
    dealerships = Dealership.query.all()
    return jsonify([{
        'id': dealership.id,
        'name': dealership.name,
        'location': dealership.location
    } for dealership in dealerships])

@app.route('/cars', methods=['GET'])
def get_cars():
    cars = Car.query.all()
    return jsonify([{
        'id': car.id,
        'make': car.make,
        'model': car.model,
        'year': car.year,
        'price': car.price,
        'dealership_id': car.dealership_id
    } for car in cars])

@app.route('/dealerships', methods=['POST'])
def add_dealership():
    data = request.json
    new_dealership = Dealership(name=data['name'], location=data['location'])
    db.session.add(new_dealership)
    db.session.commit()
    return jsonify({'message': 'Dealership added successfully'}), 201

@app.route('/cars', methods=['POST'])
def add_car():
    data = request.json
    new_car = Car(
        make=data['make'],
        model=data['model'],
        year=data['year'],
        price=data['price'],
        dealership_id=data['dealership_id']
    )
    db.session.add(new_car)
    db.session.commit()
    return jsonify({'message': 'Car added successfully'}), 201

@app.route('/serviceappointments', methods=['GET'])
def get_serviceappointments():
    services = ServiceAppointment.query.all()
    return jsonify([{
        'id': service.id,
        'description': service.description,
        'price': service.price
    } for service in services])

@app.route('/serviceappointments', methods=['POST'])
def add_serviceappointment():
    data = request.json
    new_service = ServiceAppointment(
        description=data['description'],
        price=data['price']
    )
    db.session.add(new_service)
    db.session.commit()
    return jsonify({'message': 'Service appointment added successfully'}), 201

@app.route('/add-to-cart', methods=['POST'])
def add_to_cart():
    data = request.json
    customer_id = data.get('customer_id')
    item_type = data.get('item_type')  # 'car' or 'service'
    item_id = data.get('item_id')
    quantity = data.get('quantity', 1)  # Default quantity to 1 if not provided

    # Validate input data
    if not customer_id or not item_type or not item_id:
        return jsonify({'error': 'Customer ID, Item Type, and Item ID are required'}), 400

    # Check if the item exists and add to cart
    if item_type == 'car':
        item = Car.query.get(item_id)
    elif item_type == 'service':
        item = ServiceAppointment.query.get(item_id)
    else:
        return jsonify({'error': 'Invalid item type'}), 400

    if not item:
        return jsonify({'error': 'Item not found'}), 404

    # Create or update cart item
    cart_item = Cart.query.filter_by(customer_id=customer_id, item_type=item_type, item_id=item_id).first()
    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = Cart(customer_id=customer_id, item_type=item_type, item_id=item_id, quantity=quantity)
        db.session.add(cart_item)

    db.session.commit()
    return jsonify({'message': 'Item added to cart successfully'}), 201


@app.route('/cart', methods=['GET'])
def get_cart():
    customer_id = request.args.get('customer_id')
    cart_items = Cart.query.filter_by(customer_id=customer_id).all()

    items_in_cart = []
    for item in cart_items:
        if item.item_type == 'car':
            car = Car.query.get(item.item_id)
            if car:
                items_in_cart.append({
                    'id': item.id,
                    'item_type': 'car',
                    'item': {
                        'make': car.make,
                        'model': car.model,
                        'year': car.year,
                        'price': car.price
                    },
                    'quantity': item.quantity
                })
        elif item.item_type == 'service':
            service = ServiceAppointment.query.get(item.item_id)
            if service:
                items_in_cart.append({
                    'id': item.id,
                    'item_type': 'service',
                    'item': {
                        'description': service.description,
                        'price': service.price
                    },
                    'quantity': item.quantity
                })

    return jsonify(items_in_cart)

@app.route('/cart/<int:id>', methods=['DELETE'])
def remove_from_cart(id):
    cart_item = Cart.query.get(id)
    if not cart_item:
        return jsonify({'message': 'Cart item not found'}), 404

    db.session.delete(cart_item)
    db.session.commit()
    return jsonify({'message': 'Cart item removed successfully'}), 200

@app.route('/sales', methods=['GET'])
def get_sales():
    sales = Sale.query.all()
    sales_list = []
    for sale in sales:
        car = Car.query.get(sale.car_id)
        customer = Customer.query.get(sale.customer_id)
        sales_list.append({
            'id': sale.id,
            'car': {
                'make': car.make,
                'model': car.model,
                'year': car.year,
                'price': car.price
            },
            'customer': {
                'name': customer.name,
                'email': customer.email
            },
            'date': sale.date.strftime('%Y-%m-%d %H:%M:%S')
        })
    return jsonify(sales_list)


@app.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return jsonify([{
        'id': customer.id,
        'name': customer.name,
        'email': customer.email
    } for customer in customers])

@app.route('/customers/<int:customer_id>/reviews', methods=['GET'])
def get_reviews(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    reviews = Review.query.filter_by(customer_id=customer_id).all()
    return jsonify([{
        'id': review.id,
        'comment': review.comment,
        'rating': review.rating,
        'created_at': review.created_at.strftime('%Y-%m-%d %H:%M:%S')
    } for review in reviews])

def seed_dummy_data():
    db.drop_all()
    db.create_all()

    customer1 = Customer(name='John Doe', email='john.doe@example.com')
    customer2 = Customer(name='Jane Smith', email='jane.smith@example.com')
    db.session.add_all([customer1, customer2])
    db.session.commit()

    review1 = Review(customer_id=customer1.id, comment='Excellent service!', rating=5)
    review2 = Review(customer_id=customer1.id, comment='Very satisfied with the purchase.', rating=4)
    review3 = Review(customer_id=customer2.id, comment='Average experience.', rating=3)
    db.session.add_all([review1, review2, review3])
    db.session.commit()