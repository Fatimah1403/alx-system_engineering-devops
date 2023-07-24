#!/usr/bin/python3
""" Gathering information about an employee_todo using API"""
import requests as req
import sys

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    user_id = req.get(url + 'users/{}'.faormat(sys.argv[1])).json()
    to_dos = req.get(url + 'todos', params={'userId': sys.argv[1]}).json()

    # print(to_do)
    completed = [title.get("title") for title in to_dos if
                 title.get('completed') is True]
    print(completed)
    print("Employee {} is done with tasks({}/{}):".format(user_id.get("name"),
                                                          len(competed),
                                                          len(to_dos)))
    [print("\t {}".format(title)) for title in completed]
