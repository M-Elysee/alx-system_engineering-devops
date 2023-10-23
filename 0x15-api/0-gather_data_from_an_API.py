#!/usr/bin/python3
"""a Python script that, using REST API, for a given employee ID,
   returns information about his/her TODO list progress
"""
from requests import get
import sys


if __name__ == '__main__':
    employee = get('https://jsonplaceholder.typicode.com/users/{}'
                   .format(sys.argv[1])).json()
    todos = get('https://jsonplaceholder.typicode.com/todos',
                params={"userId": sys.argv[1]}).json()
    done = [todo["title"] for todo in todos if todo["completed"]]
    print("Employee {} is done with tasks({}/{}"
          .format(employee['name'], len(done), len(todo)))
    print("\t {}".format(title for title in done))
