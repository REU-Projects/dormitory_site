from dormitory_site import server
from dormitory_site.models import base, users


base.Base.metadata.create_all(bind=server.engine)
session = server.Session()



print('DB created!')