from application import db

class Customer(db.Model):
    cust_id = db.Column(db.Integer, primary_key = True)
    forename = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    address = db.Column(db.String(50))
    dob = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(30), nullable=False)
    customer_orders = db.relationship('Order', backref='customer')
    def __str__(self):
        return f"{self.forename} {self.surname}, {self.dob}, {self.address}, {self.email}"

class Order(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.Date, nullable=False)
    cust_id = db.Column(db.Integer, db.ForeignKey('customer.cust_id'))
    order_games = db.relationship('OrderGame', backref='order')
    def __str__(self):
        return f"Placed by {self.customer.forename + ' ' + self.customer.surname} on {self.order_date}"

class OrderGame(db.Model):
    order_game_id = db.Column(db.Integer, primary_key = True)
    quantity = db.Column(db.Integer, nullable = False)
    order_id = db.Column(db.Integer, db.ForeignKey('order.order_id'))
    game_id = db.Column(db.Integer, db.ForeignKey('game.game_id'))
    def __str__(self):
        return f"order {self.order_id}: {self.quantity} x game {self.game_id}"

class Game(db.Model):
    game_id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(20), nullable=False)
    unit_price = db.Column(db.Float, nullable=False)
    rating = db.Column(db.Float)
    age_rating = db.Column(db.Integer, nullable=False)
    game_orders = db.relationship('OrderGame', backref='game')
    def __str__(self):
        return f"{self.title}, £{self.unit_price}. Rated {self.rating}/10. Suitable for ages {self.age_rating}+"