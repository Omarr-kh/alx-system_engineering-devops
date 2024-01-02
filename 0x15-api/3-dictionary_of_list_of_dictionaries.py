#!/usr/bin/python3
""" export data in the JSON format. """
import json
import requests


if __name__ == '__main__':
    url = f'https://jsonplaceholder.typicode.com/users/'
    users = requests.get(url).json()

    users_dict = {}

    todos_url = 'https://jsonplaceholder.typicode.com/todos/'
    todos = requests.get(url).json()

    for user in users:
        user_id = user.get('id')
        username = user.get('username')

        user_tasks = [task for task in todos if task.get('userId') == user_id]

        tasks_json = []
        for task in user_tasks:
            entry = {'username': username, 'task': task.get('title'),
                     'completed': task.get('completed')}
            tasks_json.append(entry)

        users_dict[f'{user_id}'] = tasks_json

    with open('todo_all_employees.json', 'w') as f:
        json.dump(users_dict, f)
