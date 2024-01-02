#!/usr/bin/python3
''' gather data from an api '''
import json
from requests import get
from sys import argv


if __name__ == "__main__":
    data = get('https://jsonplaceholder.typicode.com/todos/').json()
    user_id = int(argv[1])
    total = 0
    tasks = []

    employee = get(f'https://jsonplaceholder.typicode.com/users/{user_id}')
    e_name = employee.json().get("username")

    for task in data:
        if task.get('userId') == user_id:
            entry = {"task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": e_name}
            tasks.append(entry)

    employee_dict = {"f{user_id}" : tasks}

    with open(f'{user_id}.json', 'w') as f:
        json.dump(employee_dict, f)
