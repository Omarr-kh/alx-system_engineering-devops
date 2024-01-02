#!/usr/bin/python3
''' gather data from an api '''
from requests import get
from sys import argv


if __name__ == "__main__":
    data = get('https://jsonplaceholder.typicode.com/todos/').json()
    total = 0
    tasks = []
    employees = get('https://jsonplaceholder.typicode.com/users').json()

    for i in employees:
        if i.get('id') == int(argv[1]):
            employee = i.get('name')
            break

    for task in data:
        if task.get('userId') == int(argv[1]):
            total += 1

            if task.get('completed') is True:
                tasks.append(task.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(employee, len(tasks),
                                                          total))

    for i in tasks:
        print("\t {}".format(i))
