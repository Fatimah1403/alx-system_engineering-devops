#!/usr/bin/python3
""" queries the Reddit API and prints the titles of the first 10
hotposts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """A function that prints the titles of the
    first 10 hot posts listed for a given subreddit.
        Prototype: def top_ten(subreddit)
        If not a valid subreddit, print None


    """
    url = "https://www.reddit.com/r/{}/hot".format(subreddit)
    first_ten = {"limit": 10}

    headers = {
            "User-Agent": 'Google chrome version 115.0.5790.171'
    }

    response = get(url, headers=headers first_ten=first_ten,
                   allow_redirects=False)
    result = request.json()

    if response.status_code == 404:
        print("None")
        return
    my_data = result.get('data').get('children')

    for d in my_data:
        print(d.get('data').get('title'))
