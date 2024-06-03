#!/usr/bin/python3
"""
A scribt that uses a given employee ID,
export information about his/her TODO list progress to CSV file
"""

import csv
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
            [
                argv[1],
                name,
                todo.get('completed'),
                todo.get('title')
            ]
        )
    csv_file = '{}.csv'.format(argv[1])
    with open(csv_file, mode='w') as file:
        writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow(task)
