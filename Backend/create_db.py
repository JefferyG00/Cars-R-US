from app import app, db
from models import Car, Dealership, Customer, Sale, ServiceAppointment

with app.app_context():
    db.create_all()
