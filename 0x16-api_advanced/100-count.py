#!/usr/bin/python3
"""reddit api"""

import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """Prints counts of given words found in hot posts of a given subreddit.
    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        instances (obj): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
        count (int): The parameter of results matched thus far.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "Google chrome version 115.0.5790.171"
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    try:
        results = response.json()
        if response.status_code == 404:
            raise Exception
        except exception:
            print("")
            return

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        title = c.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                time = len([t for t in title if t == word.lower()])
                if instances.get(word) is None:
                    instances[word] = time
                else:
                    instances[word] += time

    if after is None:
        if len(instances) == 0:
            print("")
            return

        instances = sorted(instances.items(), key=lamda kv: (-kv[1], kv[0]))
        [print("{}:{}".format(k, v)) for k, v in instances]
    else:
        count_words(subreddit, word_list, instances, after, count)
