#!/usr/bin/python3
"""a Python script that, using REST API, for a given employee ID,
   returns information about his/her TODO list progress
"""
import json
from requests import get
import sys


if __name__ == '__main__':
    employee = get('https://jsonplaceholder.typicode.com/users/{}'
                   .format(sys.argv[1])).json()
    todos = get('https://jsonplaceholder.typicode.com/todos',
                params={"userId": sys.argv[1]}).json()
    with open("{}.json".format(sys.argv[1]), "w") as j_file:
        json.dump({sys.argv[1]: [{"task": todo['title'],
                                  "completed": todo['completed'],
                                  "username": employee['name']}
                                 for todo in todos]}, j_file)
