import os
import json
filename = "students.json"

"""
    ALGORITHM
    Read students from file
    Filter the students using ID
    Change the student data using to_change and value
    Write the student data
    continue or not
"""


def update(id, to_change, value):
        with open(filename, "r") as fp:
            students = json.load(fp)
        student = list(filter(lambda x: x['id'] == id, students))               # checking id from the list
        student = student[0]
        index_of_students = students.index(student)
        change = students[index_of_students]
        change[to_change] = value

        with open(filename, 'w') as fp:
                json.dump(students, fp, indent=2)
        cont = input("The student has been updated. Do you want to continue? (y/n)")
        return True if cont.lower() == 'y' else False