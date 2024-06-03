#!/usr/bin/python3
"""
A scribt that uses a given employee ID,
export information about his/her TODO list progress to json file
"""

from json import dump
import requests


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/users/'
    respose = requests.get(url)
    users = respose.json()
    data = {}
    for user in users:
        user_id = user.get('id')
        name = user.get('username')
        respose = requests.get(url + str(user_id) + '/todos')
        todos = respose.json()
        tasks = []
        for todo in todos:
            tasks.append(
                {
                    "username": name,
                    "task": todo.get('title'),
                    "completed": todo.get('completed')
                }
            )
        data[user_id] = tasks
        json_file = 'todo_all_employees.json'
        with open(json_file, mode='w') as file:
            dump(data, file)
