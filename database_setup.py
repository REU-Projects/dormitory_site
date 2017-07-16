from dormitory_site.server import db
from dormitory_site.models import users 
db.create_all()

vasya = users.User("Zufra", "FMESI", "1", "417")

db.session.add(vasya)
db.session.commit()

print("DB created!")