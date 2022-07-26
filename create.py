from application import db
from application.models import Customer, Game, Order, OrderGame
from datetime import date

db.drop_all()
db.create_all()

user1 = Customer(forename="Bob", surname="Smith", address="123 Fake St.", dob=date(1997, 3, 11), email="bobsmith@example.com")
game1 = Game(title="Xtreme Chess", unit_price=19.99, rating=6.3, age_rating=18)
order1 = Order(order_date=date(2022,7,25), cust_id=1)
order_game_1 = OrderGame(quantity = 2, order_id = 1, game_id = 1)
db.session.add(user1)
db.session.add(game1)
db.session.add(order1)
db.session.add(order_game_1)
db.session.commit()

print(user1)
print(game1)
print(order1)
print(order1.customer)
print(order_game_1)
print(order_game_1.order)
print(order_game_1.game)