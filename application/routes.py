from flask import request, redirect, url_for, render_template
from application import app, db
from application.models import *
from datetime import date

def age(customer):
    return (date.today() - customer.dob).days // 365

@app.route('/')
def index():
    return render_template('home.html')

# CRUD - create, read, update, delete
# Create
@app.route('/add-customer/<forename>-<surname>/<address>/<dob>/<email>')
def create_customer(forename, surname, address, dob, email):
    date_values = map(int, dob.split('-'))
    dob_date = date(*date_values)
    new_customer = Customer(forename=forename, surname=surname, address=address, dob=dob_date, email=email)
    db.session.add(new_customer)
    db.session.commit()
    return "added customer"

# Read
@app.route('/get-customers')
def view_customers():
    customers = Customer.query.order_by(Customer.forename).all()
    return render_template('view_all_customers.html', customers=list(customers))

@app.route('/get-cust-by-name/<name>')
def view_custs_by_name(name):
    customers = map(str, Customer.query.filter(Customer.forename.like(f'%{name}%')).all())
    return '<br>'.join(customers)

@app.route('/get-cust-by-id/<int:id>')
def get_cust_by_id(id):
    customer = Customer.query.get(id)
    return render_template('cust_by_id.html', customer=customer)

@app.route('/num-customers')
def find_num_custs():
    return str(Customer.query.count())

@app.route('/avg-age')
def avg_age():
    customers = Customer.query.all()
    customer_ages = map(age, customers)
    return str(sum(customer_ages) // Customer.query.count())

# update
@app.route('/update-customer/<int:id>/<attribute>/<new_val>')
def update_cust(id, attribute, new_val):
    customer_to_update = Customer.query.get(id)
    if attribute == 'dob':
        new_val = date(*(map(int, new_val.split('-'))))
    setattr(customer_to_update, attribute, new_val)
    db.session.commit()
    return redirect(url_for('view_customers'))

# delete
@app.route('/delete-customer/<int:id>')
def delete_customer(id):
    cust_to_delete = Customer.query.get(id)
    db.session.delete(cust_to_delete)
    db.session.commit()
    return redirect(url_for('view_customers'))