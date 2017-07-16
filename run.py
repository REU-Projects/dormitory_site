#!flask/bin/python
from dormitory_site.server import app

port = int(os.environ.get('PORT', 5000))

if port == 5000:
    app.debug = True

app.run(host='0.0.0.0', port=port)