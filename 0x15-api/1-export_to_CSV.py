#!/usr/bin/python3
"""a Python script that, using REST API, for a given employee ID,
   returns information about his/her TODO list progress
"""
import csv
from requests import get
import sys


if __name__ == '__main__':
    userId = sys.argv[1]
    employee = get('https://jsonplaceholder.typicode.com/users/{}'
                   .format(userId)).json()
    todos = get('https://jsonplaceholder.typicode.com/todos',
                params={"user_id": userId}).json()

    with open("{}.csv".format(userId), "w", newline="") as csv_f:
        wr = csv.writer(csv_f, quoting=csv.QUOTE_ALL)
        [wr.writerow([userId, employee['name'], todo['completed'],
                      todo['title']]) for todo in todos]
