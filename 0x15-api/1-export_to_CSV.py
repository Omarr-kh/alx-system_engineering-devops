#!/usr/bin/python3
''' gather data from an api '''
import csv
from requests import get
from sys import argv


if __name__ == "__main__":
    data = get('https://jsonplaceholder.typicode.com/todos/').json()
    user_id = int(argv[1])
    total = 0
    rows = []
    employee = get(f'https://jsonplaceholder.typicode.com/users/{user_id}')
    e_name = employee.json().get("username")

    for task in data:
        if task.get('userId') == user_id:
            row = [user_id, e_name, task.get("completed"), task.get("title")]
            rows.append(row)

    with open(f'{user_id}.csv', 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(rows)
