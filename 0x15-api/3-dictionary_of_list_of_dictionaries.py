#!/usr/bin/python3
""" export data in the JSON format. """
import json
import requests

if __name__ == '__main__':
    employees_url = 'https://jsonplaceholder.typicode.com/users/'
    employee_list = requests.get(employees_url).json()

    all_tasks_json = {}

    for employee in employee_list:
        emp_id = employee.get('id')
        emp_username = employee.get('username')

        tasks_url = 'https://jsonplaceholder.typicode.com/todos/'
        all_tasks = requests.get(tasks_url).json()

        filtered_tasks = [
            task for task in all_tasks if task.get('userId') == emp_id]

        formatted_tasks = []
        for task in filtered_tasks:
            task_info = {'username': emp_username, 'task': task.get('title'),
                         'completed': task.get('completed')}
            formatted_tasks.append(task_info)

        all_tasks_json[f'{emp_id}'] = formatted_tasks

    with open('todo_all_employees.json', 'w') as f:
        json.dump(all_tasks_json, f)
