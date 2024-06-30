from app import app, db
from models import ServiceAppointment

def seed_services():
    services = [
        {'description': 'Oil Change', 'price': 29.99},
        {'description': 'Tire Rotation', 'price': 19.99},
        {'description': 'Car Wash', 'price': 14.99}
    ]

    for service in services:
        new_service = ServiceAppointment(description=service['description'], price=service['price'])
        db.session.add(new_service)
    
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        seed_services()
