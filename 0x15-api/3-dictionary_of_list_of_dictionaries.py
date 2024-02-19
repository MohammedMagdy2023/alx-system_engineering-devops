#!/usr/bin/python3
"""fetches information from JSONplaceholder API and exports to JSON"""

from json import dump
from requests import get

if __name__ == "__main__":
    api = "https://jsonplaceholder.typicode.com"

    employee = get(api + "/users").json()

    data_dic = {}
    for user in employee:
        todo_list = []

        todos = api + "/user/{}/todos".format(user.get("id"))
        name_url = api + "/users/{}".format(user.get("id"))

        todo_lst = get(todos).json()
        emp_name = get(name_url).json()
        for todo in todo_lst:
            todo_dict = {}
            todo_dict.update({"username": emp_name.get("username"),
                              "task": todo.get("title"),
                              "completed": todo.get("completed")})
            todo_list.append(todo_dict)

        data_dic.update({user.get("id"): todo_list})

    with open("todo_all_employees.json", 'w') as f:
        dump(data_dic, f)
