#!/usr/bin/python3
"""
function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit. If no results
are found for the given subreddit, the function should return None.

"""
import requests


def recurse(subreddit, hot_list=[]):
    """Returns a list of titles of all hot posts on a given subreddit."""
     headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
