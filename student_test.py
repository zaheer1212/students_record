import pytest
import requests
import student
import json
import sys
import os.path


def test_student_records():
    data = {
        'name': 'Akash',
        'roll_num': 'std101',
        'student_id': '101'
    }
    records = requests.get('http://127.0.0.1:5000/')
    insert_records = requests.post('http://127.0.0.1:5000/', data=data)
    assert insert_records.status_code == 200
    assert records.status_code == 200