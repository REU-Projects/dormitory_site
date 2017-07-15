from dormitory_site.server import db
from dormitory_site.models import users 
db.create_all()

print("DB created!")