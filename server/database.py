
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
MYSQL_DATABASE_HOST = 'localhost'
MYSQL_DATABASE_PORT = 3306
DEBUG = True
SECRET_KEY = 'development key'
MYSQL_DATABASE_USER = 'root'
MYSQL_DATABASE_DB = 'test'
MYSQL_DATABASE_PASSWORD = 'sauran_1993'
app.config.from_object(__name__)
mysql.init_app(app)
connection = mysql.connect()
cursor = connection.cursor()
