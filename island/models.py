from island import db


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    email_address = db.Column(db.String(length=50), nullable=False)
    comment = db.Column(db.String(length=500), nullable=False)


class Applicant(db.Model):
    id = db.Column(db.Integer(), primary_key =True)
    name = db.Column(db.String(length=30), nullable=False)
    email_address = db.Column(db.String(length=50), nullable=False)
    phone_number = db.Column(db.Integer(), nullable=False)
    county = db.Column(db.String(length=20), nullable=False)
    town = db.Column(db.String(length=20), nullable=False)
    enquiry = db.Column(db.String(length=20), nullable=False)
    