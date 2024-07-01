from app import app, db
from models import Customer, Review
from sqlalchemy.orm import Session

def seed_dummy_reviews():
    with app.app_context():
        session: Session = db.session
        
        customer1 = session.get(Customer, 1)  # Replace with an existing customer ID
        customer2 = session.get(Customer, 2)  # Replace with another existing customer ID

        review1 = Review(customer_id=customer1.id, comment='Excellent service!', rating=5)
        review2 = Review(customer_id=customer1.id, comment='Very satisfied with the purchase.', rating=4)
        review3 = Review(customer_id=customer2.id, comment='Average experience.', rating=3)

        db.session.add_all([review1, review2, review3])
        db.session.commit()

if __name__ == "__main__":
    seed_dummy_reviews()

