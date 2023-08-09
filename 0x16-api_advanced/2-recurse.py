#!/usr/bin/python3
"""
function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit. If no results
are found for the given subreddit, the function should return None.

"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    param = {"after": after,
             "count": count,
             "limit": 100
             }
    request = requests.get(url, headers=headers, param=param,
                           allow_redirects=False)
    if response.status_code == 404:
        return None
    results = response.json().get('data')
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get.("title"))
    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
