#!/usr/bin/python3
"""
Python script that, using REST API,
for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys

if __name__ == "__main__":
    emp_id = sys.argv[1]

    api = "https://jsonplaceholder.typicode.com/"

    employee = requests.get(api + "users/" + emp_id)

    if employee.status_code == 200:
        emp_name = employee.json()["name"]
    else:
        print("Invalid employee ID")
        sys.exit(1)

    todo = requests.get(api + "todos?userId=" + emp_id)
    if todo.status_code == 200:
        todo_list = todo.json()
        total_tasks = len(todo_list)
        completed_tasks = 0
        completed_titles = []
        for task in todo_list:
            if task["completed"]:
                completed_tasks += 1
                completed_titles.append(task["title"])
    else:
        print("Could not get the TODO list")
        sys.exit(1)

    print("Employee {} is completed with tasks({}/{}):"
          .format(emp_name, completed_tasks, total_tasks))
    for title in completed_titles:
        print("\t " + title)
