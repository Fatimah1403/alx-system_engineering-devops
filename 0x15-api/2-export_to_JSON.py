#!/usr/bin/python3
"""Exporting the employer to_do list in json format
"""
import json
import requests as req
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = req.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = req.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": el.get("title"),
                "completed": el.get("completed"),
                "username": "username"
                } for el in todos]}, jsonfile)
