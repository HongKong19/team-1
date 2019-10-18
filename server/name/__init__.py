from flask import Flask;
from flaskext.mysql import MySQL;

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
# app.config['MYSQL_DATABASE_PORT'] = '3306'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'user_db'

mysql.init_app(app)

conn = mysql.connect()

# from . import lottery
from . import login

