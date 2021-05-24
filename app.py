
from flask import Flask, request, render_template
import pymysql
import os

db_host = os.environ['MYSQL_SERVICE_PORT_3306_TCP_ADDR']
db_user = 'root'
db_pass = os.environ['MYSQL_ROOT_PASSWORD']
db_name = 'sakila'


db = pymysql.connect(host=db_host, user=db_user, password=db_pass, database=db_name)

app = Flask(__name__)

@app.route('/')
def someName():
    cursor = db.cursor()
    sql = "select * from actor_info LIMIT 10"
    cursor.execute(sql)
    results = cursor.fetchall()
    result_list = list(results)
    results = [ list(element) for element in result_list ]
    print (results)
    return tabulate(results, tablefmt="html")

if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host='0.0.0.0',port='8080')
