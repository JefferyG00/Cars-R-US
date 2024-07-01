# insert_sample_data.py
from app import app, db
from models import Car, Dealership

with app.app_context():
    dealership = Dealership(name='Sample Dealership', location='123 Main St')
    db.session.add(dealership)
    db.session.commit()

    car = Car(make='Toyota', model='Corolla', year=2020, price=20000, dealership_id=dealership.id)
    db.session.add(car)
    db.session.commit()

    print("Sample data added successfully!")

    
