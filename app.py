
from flask import Flask, request, render_template
import pymysql


db_host = os.environ['MYSQL_SERVICE_PORT_3306_TCP_ADDR']
db_user = 'root'
db_pass = os.environ['MYSQL_ROOT_PASSWORD']
db_name = 'sakila'


db = pymysql.connect(db_host, db_user, db_pass, db_name)

app = Flask(__name__)
api = Api(app)

@app.route('/')
def someName():
    cursor = db.cursor()
    sql = "show tables"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template('index.html', results=results)

if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host='0.0.0.0',port='8080')
