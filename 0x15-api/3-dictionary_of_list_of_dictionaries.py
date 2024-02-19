#!/usr/bin/python3
"""export data in JSON format"""
import json
import requests


def to_json():
    """creates a json file of a user data"""
    user_url = 'https://jsonplaceholder.typicode.com/users'
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    users = requests.get(user_url).json()
    todos = requests.get(todo_url).json()
    task_dict = {}
    filename = "todo_all_employees.json"
    for user in users:
        name = user['username']
        user_id = user['id']
        task_list = []
        for todo in todos:
            if todo['userId'] == user_id:
                todo_dict = {}
                todo_dict["username"] = name
                todo_dict["task"] = todo['title']
                todo_dict["completed"] = todo['completed']
                task_list.append(todo_dict)
        task_dict[str(user_id)] = task_list
    with open(filename, 'w') as file:
        json.dump(task_dict, file)


if __name__ == '__main__':
    to_json()
