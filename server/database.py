from flaskext.mysql import MySQL

from server.config import DATABASE_CRED

mysql = MySQL()


def init_mysql(app):
    app.config['MYSQL_DATABASE_USER'] = DATABASE_CRED['USER']
    app.config['MYSQL_DATABASE_PASSWORD'] = DATABASE_CRED['PASSWORD']
    app.config['MYSQL_DATABASE_DB'] = DATABASE_CRED['DB']
    app.config['MYSQL_DATABASE_HOST'] = DATABASE_CRED['HOST']
    mysql.init_app(app)


def db_connect():
    conn = mysql.connect()
    return conn


def db_disconnect(connection):
    connection.close()



