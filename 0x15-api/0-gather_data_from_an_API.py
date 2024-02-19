#!/usr/bin/python3
"""returns information about an employee todo list"""
import requests
import sys


def get_todo(userId):
    """gets information about a user todo using userID"""
    url = 'https://jsonplaceholder.typicode.com/todos'
    users_url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    users = requests.get(users_url)
    todos = response.json()
    users = users.json()
    completed = 0
    task_no = 0
    name = ''
    tasks = []
    for todo in todos:
        if todo['userId'] == userId:
            if todo['completed'] is True:
                completed += 1
                tasks.append(todo['title'])
            task_no += 1
    for user in users:
        if user['id'] == userId:
            name = user['name']
            break
    print(f"Employee {name} is done with tasks({completed}/{task_no})")
    for task in tasks:
        print(f"\t {task}")


get_todo(int(sys.argv[1]))
