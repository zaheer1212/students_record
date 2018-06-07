from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    roll_no = db.Column(db.String(120), unique=True)

    def __init__(self, name, roll_num):
        self.name = name
        self.roll_no = roll_num


class StudentSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('name', 'roll_num')


student_schema = StudentSchema()
students_schema = StudentSchema(many=True)


# endpoint to create new user
@app.route("/student", methods=["POST"])
def add_user():
    name = request.json['name']
    roll_num = request.json['roll_num']

    new_user = Student(name, roll_num)

    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user)


# endpoint to show all students
@app.route("/student", methods=["GET"])
def get_user():
    all_users = Student.query.all()
    result = student_schema.dump(all_users)
    return jsonify(result.data)


# endpoint to get user detail by id
@app.route("/student/<id>", methods=["GET"])
def user_detail(id):
    student = Student.query.get(id)
    return student_schema.jsonify(student)


# endpoint to update user
@app.route("/student/<id>", methods=["PUT"])
def user_update(id):
    student = Student.query.get(id)
    name = request.json['name']
    roll_num = request.json['roll_num']

    student.roll_num = roll_num
    student.name = name

    db.session.commit()
    return student_schema.jsonify(student)


# endpoint to delete user
@app.route("/user/<id>", methods=["DELETE"])
def user_delete(id):
    student = Student.query.get(id)
    db.session.delete(student)
    db.session.commit()

    return student_schema.jsonify(student)


if __name__ == '__main__':
    app.run(debug=True)
