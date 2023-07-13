#!/usr/bin/python3
"""This function returns all the hot posts from a given sureddit"""

import requests


def recurse(subreddit, hot_list=[]):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?list={hot_list}"
    headers = {"User-Agent": "My User Agent 1.0"}
    feedback = requests.get(url, headers=headers)

    if feedback.status_code != 200:
        print(None)
    else:
        data1 = feedback.json().get("data").get("children")
        for post in data1:
            data2 = hot_list.append(post.get("data").get("title"))
            print(data2)
