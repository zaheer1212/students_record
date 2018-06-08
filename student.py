from flask import Flask
from flask_restful import Resource, Api
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flaskext.mysql import MySQL
import MySQLdb
import os


app = Flask(__name__)
api = Api(app)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'bugs123'
app.config['MYSQL_DATABASE_DB'] = 'students'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)
db = MySQLdb.connect(host="localhost", user="root", passwd="bugs123", db="students")
cur = db.cursor()

# endpoint to create new user
class StudendtsRecord(Resource):
    def get(self):
        print 'IN THIS FUNCTION'
        cur.execute('''select * from std_record''')
        r = [dict((cur.description[i][0], value)
                  for i, value in enumerate(row)) for row in cur.fetchall()]
        print r
        return jsonify({'myCollection' : r})

    def post(self):
        print("Create Record")
        try:
            name = request.form['name']
            roll_num = request.form['roll_num']
            print name, roll_num
            cur.execute('''INSERT INTO `students`.`std_record`
            (`name`,
            `roll_num`)
            VALUES
            (%s,%s)''',(name, roll_num))
            db.autocommit(on=True)
            return 'Student Added to DATABASE'
        except Exception as e:
           return(str(e))

    def delete(self):
        print("Delete Record")
        try:
            roll_num = request.form['roll_num']
            print roll_num
            try:
                cur.execute('''DELETE FROM `students`.`std_record`
                WHERE id > 0 and roll_num=%s;''', (roll_num))
            except Exception as e:
                print '============================'
                print e
                print '============================'
            print "DELETED"
            return 'Record Deleted'
        except Exception as e:
            return(str(e))

api.add_resource(StudendtsRecord, '/')

if __name__ == '__main__':
    app.run(debug=True)
