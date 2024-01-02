#!/usr/bin/python3
""" export data in the JSON format. """
import json
import requests

if __name__ == '__main__':
    employees_url = 'https://jsonplaceholder.typicode.com/users/'
    employees_response = requests.get(employees_url)
    employee_list = employees_response.json()

    all_tasks_json = {}

    for employee in employee_list:
        emp_id = employee.get('id')
        emp_username = employee.get('username')

        tasks_url = 'https://jsonplaceholder.typicode.com/todos/'
        tasks_response = requests.get(tasks_url)
        all_tasks = tasks_response.json()
        filtered_tasks = [
            task for task in all_tasks if task.get('userId') == emp_id]

        formatted_tasks = []
        for task in filtered_tasks:
            task_info = {'username': emp_username, 'task': task.get('title'),
                         'completed': task.get('completed')}
            formatted_tasks.append(task_info)

        all_tasks_json[f'{emp_id}'] = formatted_tasks

    # Save the information to a JSON file:
    with open('todo_all_employees.json', 'w') as f:
        json.dump(all_tasks_json, f)
