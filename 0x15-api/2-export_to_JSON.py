#!/usr/bin/python3
"""
A scribt that uses a given employee ID,
export information about his/her TODO list progress to json file
"""

from json import dump
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    respose = requests.get(url)
    user = respose.json()
    name = user.get('username')
    respose = requests.get(url + '/todos')
    todos = respose.json()
    tasks = []
    for todo in todos:
        tasks.append(
            {
                "task": todo.get('title'),
                "completed": todo.get('completed'),
                "username": name
            }
        )
    json_file = '{}.json'.format(argv[1])
    with open(json_file, mode='w') as file:
        dump({argv[1]: tasks}, file)
