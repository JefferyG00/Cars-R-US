from datetime import datetime
from app import app, db
from models import Car, Dealership, Customer, Sale

def create_fake_data():
    # Create Dealership
    dealership = Dealership(name='Test Dealership', location='Test Location')
    db.session.add(dealership)
    db.session.commit()

    # Create Cars
    car1 = Car(make='Toyota', model='Camry', year=2020, price=24000, dealership_id=dealership.id)
    car2 = Car(make='Honda', model='Accord', year=2019, price=22000, dealership_id=dealership.id)
    db.session.add(car1)
    db.session.add(car2)
    db.session.commit()

    # Check if Customers exist before creating
    customer1 = Customer.query.filter_by(name='John Doe').first()
    if not customer1:
        customer1 = Customer(name='John Doe', email='john.doe@example.com')
        db.session.add(customer1)

    customer2 = Customer.query.filter_by(name='Jane Smith').first()
    if not customer2:
        customer2 = Customer(name='Jane Smith', email='jane.smith@example.com')
        db.session.add(customer2)

    db.session.commit()

    # Create Sales (assuming cars and customers are created correctly)
    sale1 = Sale.query.filter_by(car_id=car1.id, customer_id=customer1.id).first()
    if not sale1:
        sale1 = Sale(car_id=car1.id, customer_id=customer1.id, date=datetime.now())
        db.session.add(sale1)

    sale2 = Sale.query.filter_by(car_id=car2.id, customer_id=customer2.id).first()
    if not sale2:
        sale2 = Sale(car_id=car2.id, customer_id=customer2.id, date=datetime.now())
        db.session.add(sale2)

    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        create_fake_data()
