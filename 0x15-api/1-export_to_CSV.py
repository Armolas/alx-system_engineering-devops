#!/usr/bin/python3
"""exports user data in csv format"""
import requests
import sys


def create_csv(user_id):
    user_url = 'https://jsonplaceholder.typicode.com/users'
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    users = requests.get(user_url)
    users = users.json()
    todos = requests.get(todo_url)
    todos = todos.json()
    filename = f"{str(user_id)}.csv"
    for user in users:
        if user['id'] == user_id:
            name = user['name']
            break
    with open(filename, 'w') as file:
        for todo in todos:
            if todo['userId'] == user_id:
                line = f"\"{str(user_id)}\",\"{str(name)}\",\
\"{todo['completed']}\",\"{todo['title']}\"\n"
                file.write(line)


if __name__ == '__main__':
    create_csv(int(sys.argv[1]))
