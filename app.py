# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask,render_template, request
from flask_mysqldb import MySQL
from tabulate import tabulate
import os
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

mysql = MySQL()

app.config['MYSQL_HOST'] = os.environ['MYSQL_SERVICE_PORT_3306_TCP_ADDR']
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = os.environ['MYSQL_ROOT_PASSWORD']
app.config['MYSQL_DB'] = 'sakila'

mysql.init_app(app)


conn = mysql.connect()
cursor =conn.cursor()

cursor.execute("show tables")
data = cursor.fetchone()

print(data)
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    table = [["Sun",696000,1989100000],["Earth",6371,5973.6],["Moon",1737,73.5],["Mars",3390,641.85]]

    return tabulate(table, tablefmt='html')

# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host='0.0.0.0',port='8080')
