#!/usr/bin/python3
"""export data in JSON format"""
import json
import requests
import sys


def to_json(user_id):
    """creates a json file of a user data"""
    user_url = 'https://jsonplaceholder.typicode.com/users'
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    users = requests.get(user_url).json()
    todos = requests.get(todo_url).json()
    task_list = []
    task_dict = {}
    filename = f"{user_id}.json"
    for user in users:
        if user['id'] == user_id:
            name = user['username']
    for todo in todos:
        if todo['userId'] == user_id:
            todo_dict = {}
            todo_dict["task"] = todo['title']
            todo_dict["completed"] = todo['completed']
            todo_dict["username"] = name
            task_list.append(todo_dict)
    task_dict[str(user_id)] = task_list
    with open(filename, 'w') as file:
        json.dump(task_dict, file)


if __name__ == '__main__':
    to_json(int(sys.argv[1]))
