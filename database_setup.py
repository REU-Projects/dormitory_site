from dormitory_site.server import db
from dormitory_site.models import users 
db.create_all()

student = users.User("Some student", "Some faculty", "1", "1")

db.session.add(student)
db.session.commit()

print("DB created!")