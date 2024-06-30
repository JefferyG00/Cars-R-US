from app import app, db
from flask import request, jsonify
from models import Car, Dealership, Customer, Sale, ServiceAppointment, Cart

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

@app.route('/cart', methods=['GET'])
def get_cart():
    customer_id = request.args.get('customer_id')
    cart_items = Cart.query.filter_by(customer_id=customer_id).all()
    return jsonify([{
        'id': item.id,
        'service_id': item.service_id,
        'service_description': item.service.description,
        'quantity': item.quantity
    } for item in cart_items])

@app.route('/cart', methods=['POST'])
def add_to_cart():
    data = request.json
    new_cart_item = Cart(
        customer_id=data['customer_id'],
        service_id=data['service_id'],
        quantity=data['quantity']
    )
    db.session.add(new_cart_item)
    db.session.commit()
    return jsonify({'message': 'Service added to cart successfully'}), 201

@app.route('/cart/<int:id>', methods=['DELETE'])
def remove_from_cart(id):
    cart_item = Cart.query.get(id)
    if not cart_item:
        return jsonify({'message': 'Cart item not found'}), 404

    db.session.delete(cart_item)
    db.session.commit()
    return jsonify({'message': 'Cart item removed successfully'}), 200
