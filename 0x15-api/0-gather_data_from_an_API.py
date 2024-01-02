#!/usr/bin/python3
''' gather data from an api '''
import requests
import sys


def main():
    url = "https://jsonplaceholder.typicode.com/"
    Eid = int(sys.argv[1])
    completed = []
    data = requests.get(url + 'todos').json()

    total = 0
    for employee in data:
        if employee.get('userId') == Eid:
            if employee.get('completed'):
                completed.append(employee['title'])
            total += 1

    employee = requests.get(f'{url}users/{Eid}').json()
    name = employee.get("name")
    print(f'Employee {name} is done with tasks({len(completed)}/{total}):')
    for title in completed:
        print(f"\t {title}")


if __name__ == "__main__":
    main()
