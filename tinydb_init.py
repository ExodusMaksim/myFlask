from tinydb import TinyDB, Query


db = TinyDB('./users.json')

db.insert({'user_id': 1, 'name': 'xm', 'age': 18, 'address': '123'})
db.insert({'user_id': 2, 'name': 'zs', 'age': 28, 'address': '123'})
db.insert({'user_id': 3, 'name': 'ls', 'age': 21, 'address': '123'})


print(db.all())