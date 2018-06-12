from flask_restful import Resource, Api
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
import os

app = Flask(__name__)
app.config["MONGO_DBNAME"] = "students"                     # Name of your mongodb Database
mongo = PyMongo(app, config_prefix='MONGO')
api = Api(app)


# endpoint to create new user
class StudendtsRecord(Resource):
    def get(self):                          # Function to get all names and roll numbers of students
        data = []
        # Query to Get data of students from database.
        studnet_info = mongo.db.student_record.find({}, {"_id": 0, }).limit(10)
        for student in studnet_info:                        # Loop to get data of each student and save it in a list.
            data.append(student)
        return jsonify({"Studnets_Record": data})        # Return list of students after converting it in JSON format.

    def post(self):                         # Function to Insert Student data from post.
        try:
            if 'name' in request.form:                      # to get name of student from form data
                name = request.form['name']
            else:
                name = ''
            if 'roll_num' in request.form:                  # to get roll_number of student from form data
                roll_num = request.form['roll_num']
            else:
                roll_num = ''
            if 'id' in request.form:                        # to get roll_number of student_ID from form data
                student_id = request.form['id']
            else:
                student_id = ''
            if len(name) == 0 and len(roll_num) == 0 and len(student_id) == 0:
                return 'Form is empty at least one column value of name, roll_num or id is Necessary'
            # Query To Insert Record of Student in Database
            mongo.db.student_record.insert({"name": name, "roll_num": roll_num, "student_id": student_id})
            return 'Student Added to DATABASE'
        except Exception as e:
            return(str(e))

    def delete(self):                           # Function to Delete Student Record on base of his name.
        if 'name' in request.form:
            name = request.form['name']
        else:
            return 'Form data is not correct..'
        # Query To Delete Record of Student in Database
        mongo.db.student_record.remove({'name': name})
        return 'Record for This student is Deleted'


api.add_resource(StudendtsRecord, '/')

if __name__ == '__main__':
    app.run(debug=True)
