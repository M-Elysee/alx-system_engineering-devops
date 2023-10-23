#!/usr/bin/python3
"""a Python script that, using REST API, for a given employee ID,
   returns information about his/her TODO list progress
"""
import json
from requests import get


if __name__ == '__main__':
    employees = get('https://jsonplaceholder.typicode.com/users').json()
    todos = 'https://jsonplaceholder.typicode.com/todos'
    with open("todo_all_employees.json", "w") as j_file:
        json.dump({employee["id"]:
                   [{"username": employee["username"], "task": todo["title"],
                     "completed": todo["completed"]}
                    for todo in get(todos,
                                    params={"userId": employee["id"]}).json()]
                   for employee in employees}, j_file)
