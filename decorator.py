import os
import json
filename1 = "password.json"


def password_required(func):
    def inner_function(*args, **kwargs):
        pwd = input("Enter a password: ")
        with open(filename1, "r") as fp:
            data = json.load(fp)
        if pwd == data["password"]:
            print("You are Welcome!!")
            return func(*args, **kwargs)
        else:
            print("Your password is not match.")
    return inner_function


password_required(filename1)


