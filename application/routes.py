from flask import request, redirect, url_for
from application import app, db
from application.models import *
from datetime import date

# CRUD - create, read, update, delete
@app.route('/add-customer/<forename>-<surname>/<address>/<dob>/<email>')
def create_customer(forename, surname, address, dob, email):
    date_values = map(int, dob.split('-'))
    dob_date = date(*date_values)
    new_customer = Customer(forename=forename, surname=surname, address=address, dob=dob_date, email=email)
    db.session.add(new_customer)
    db.session.commit()
    return "added customer"

@app.route('/get-customers')
def view_customers():
    customers = map(str, Customer.query.order_by(Customer.forename).all())
    return '<br>'.join(customers)

@app.route('/get-cust-by-name/<name>')
def view_custs_by_name(name):
    customers = map(str, Customer.query.filter(Customer.forename.like(f'%{name}%')).all())
    return '<br>'.join(customers)

@app.route('/get-cust-by-id/<int:id>')
def get_cust_by_id(id):
    customer = Customer.query.get(id)
    return str(customer)

@app.route('/num-customers')
def find_num_custs():
    return str(Customer.query.count())