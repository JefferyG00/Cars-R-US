from app import db

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(80), nullable=False)
    model = db.Column(db.String(80), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    dealership_id = db.Column(db.Integer, db.ForeignKey('dealership.id'), nullable=False)
    dealership = db.relationship('Dealership', backref=db.backref('cars', lazy=True))

    def __repr__(self):
        return f'<Car {self.make} {self.model}>'

class Dealership(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<Dealership {self.name}>'

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)

class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    car = db.relationship('Car', backref='sales')
    customer = db.relationship('Customer', backref='sales')

class ServiceAppointment(db.Model):
    __tablename__ = 'service_appointment'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=True) 



class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    item_type = db.Column(db.String(50), nullable=False)  # 'car' or 'service'
    item_id = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)

    customer = db.relationship('Customer', backref='cart_items', lazy=True)

    def __repr__(self):
        return f'<Cart {self.item_type} {self.item_id}>'

