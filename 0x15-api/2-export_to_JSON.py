#!/usr/bin/python3
"""
Python script that,
using REST API,
for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import requests
import sys

if __name__ == "__main__":
    api = "https://jsonplaceholder.typicode.com/"
    emp_id = sys.argv[1]

    employee = requests.get(api + "users/" + emp_id)

    tasks = requests.get(api + "todos?userId=" + emp_id)

    emp_name = employee.json()["name"]
    todo_list = tasks.json()

    with open(emp_id + ".json", "w") as f:
        json.dump({emp_id: [{"task": task["title"],
                             "completed": task["completed"],
                             "username": emp_name} for task in todo_list]}, f)
