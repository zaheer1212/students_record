import pytest
import requests


data = [
        {
            "name": "Faiq",
            "roll_num": "std102",
            "student_id": 2
        },
        {
            "name": "Ali",
            "roll_num": "std103",
            "student_id": "3"
        }
]

def show_studetn_data():
    return data

def insert_student_record(name, id, roll_num):
    if name == 'Ali' and id == '101' and roll_num == 'std101':
        student_data = {
            'name': name,
            'roll_num': roll_num,
            'student_id': id
        }
        data.append(student_data)
        return 'Record Added'

def insert_student_record_1(name, id):
    if name == 'Ali' and id == '101':
        return 'Form is Invalid Missing Roll_Number'

def insert_student_record_2(name, roll_num):
    if name == 'Ali' and roll_num == 'std101':
        return 'Form is invalid Missing Id'

def insert_student_record_3(roll_num, id):
    if roll_num == 'std101' and id == '101':
        return 'Form is invalid Missing Name'

def delete_student_record(name):
    for value in data:
        if value['name'] == name:
            del value
        return 'Student Deleted'

def test_insert_student_record(student):
    name = 'Ali'
    id = '101'
    roll_num = 'std101'
    assert show_studetn_data() == data
    assert delete_student_record(name) == 'Student Deleted'
    assert insert_student_record(name, id, roll_num) == 'Record Added'
    assert insert_student_record_1(name, id) == 'Form is Invalid Missing Roll_Number'
    assert insert_student_record_3(roll_num, id) == 'Form is invalid Missing Name'
    assert insert_student_record_2(name, roll_num) == 'Form is invalid Missing Id'
