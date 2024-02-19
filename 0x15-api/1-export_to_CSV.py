#!/usr/bin/python3
""" Python script that,
using REST API,
for a given employee ID,
returns information about his/her TODO list progress.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    api = "https://jsonplaceholder.typicode.com/"
    emp_id = sys.argv[1]

    employee = requests.get(api + "users/" + emp_id)

    tasks = requests.get(api + "todos?userId=" + emp_id)

    emp_name = employee.json()["username"]
    todo_list = tasks.json()

    with open(emp_id + ".csv", "w") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todo_list:
            writer.writerow([emp_id, emp_name,
                            task["completed"], task["title"]])
