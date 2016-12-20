from server import app
from server.config import SERVER_CONFIG

app.run(host=SERVER_CONFIG['HOST'], debug=SERVER_CONFIG['DEBUG'], port=SERVER_CONFIG['PORT'])
