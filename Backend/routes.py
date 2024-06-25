from app import app, db
from flask import request, jsonify
from models import Car, Dealership, Customer, Sale, ServiceAppointment
from datetime import datetime


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
