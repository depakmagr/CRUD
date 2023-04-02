# import os
# import json
# filename = "students.json"
from decorator import password_required
from estd_connection import estd_connection


@password_required
def create():
    cursor = estd_connection()
    id = input("Enter the id of student ")
    name = input("Enter name of the student ")
    dept = input("Enter the department ")
    sql = f"""
            INSERT INTO STUDENT(ID, NAME, DEPARTMENT) VALUES ('{id}', '{name}','{dept}')
            """
    cursor.execute(sql)
    cont = input("A new student has been added. Do you want to continue? (y/n)")
    return True if cont.lower() == 'y' else False


    # @password_required
    # def create():
    # student = dict(id=id, name=name, department=dept)
    # if os.path.exists(filename):
    #     with open(filename, "r") as fp:
    #         # students = fp.read()
    #         students = json.load(fp)
    # else:
    #     students = []
    # students.append(student)
    #
    # with open(filename, 'w') as fp:
    #     json.dump(students, fp, indent=2)

