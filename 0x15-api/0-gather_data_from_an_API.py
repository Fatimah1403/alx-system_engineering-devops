#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = requests.get(url + "users/{}".format(sys.argv[1])).json()
    to_dos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user_id.get("name"), len(completed), len(to_dos)))
    [print("\t {}".format(c)) for c in completed]
