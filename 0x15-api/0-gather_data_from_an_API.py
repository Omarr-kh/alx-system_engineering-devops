#!/usr/bin/python3
''' gather data from an api '''
import requests
import sys


def main():
    employee_id = int(sys.argv[1])
    completed = []
    data = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    total = 0
    for employee in data:
        if employee.get('userId') == employee_id:
            if employee.get('completed'):
                completed.append(employee['title'])
            total += 1

    employee = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}').json()
    print(f'Employee {employee.get("name")} is done with tasks({len(completed)}/{total}):')
    for title in completed:
        print(f"\t {title}")


if __name__ == "__main__":
    main()
