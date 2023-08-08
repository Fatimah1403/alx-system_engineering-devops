#!/usr/bin/python3
""" querries that retuens Reddit api, the total nos of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """a function that queries the Reddit API and returns
    the number of subscribers(not active users, total subscribers)
    for a given subreddit. If an invalid subreddit is given,
    the function should return 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {
            "User-Agent": "Google chrome version 115.0.5790.171"
            }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    result = response.json().get("data")
    return result.get("subscribers")
