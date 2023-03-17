import json

password = input("Please set a password: ")
data = {"password": password}


with open("password.json", 'w') as fp:
    json.dump(data, fp, indent=2)

print("Password has been added successfully.")

