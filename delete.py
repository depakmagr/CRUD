import os
import json
filename = "students.json"

"""
    ALGORITHM
    Read the students
    Filter the particular student using id
    Remove the filtered student
    Write to file
    Continue or not
"""


def delete(id):
    with open(filename, "r") as fp:
        students = json.load(fp)
    student = list(filter(lambda x: x['id'] == id, students))
    student = student[0]
    students.remove(student)
    with open(filename, 'w') as fp:
        json.dump(students, fp, indent=2)
    cont = input("The student has been deleted. Do you want to continue? (y/n)")
    return True if cont.lower() == 'y' else False