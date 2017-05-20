from dormitory_site import server
from dormitory_site.models import base, users


base.Base.metadata.create_all(bind=server.engine)
session = server.Session()

vasiaUser = users.User("vasia", "Vasiliy Pypkin", "vasia2000")
petyaUser = users.User("petya", "Petya Pypkin", "petya2000")
session.add(vasiaUser)
session.add(petyaUser)
session.commit()

print('DB created!')