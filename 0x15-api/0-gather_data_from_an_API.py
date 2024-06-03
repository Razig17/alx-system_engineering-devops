#!/usr/bin/python3
"""
A scribt that uses a given employee ID,
returns information about his/her TODO list progress
"""

import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    respose = requests.get(url)
    user = respose.json()
    name = user.get('name')
    respose = requests.get(url + '/todos')
    todos = respose.json()
    done = []
    total = 0
    for todo in todos:
        total += 1
        if todo.get('completed'):
            done.append(todo)
    print(f"Employee {name} is done with tasks({len(done)}/{total}):")
    for todo in done:
        print("\t " + todo.get('title'))
