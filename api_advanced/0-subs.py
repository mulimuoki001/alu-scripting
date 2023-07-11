#!/usr/bin/python3
'''o-subs.py'''


import requests


def number_of_subscribers(subreddit):
    api_url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'My Bot/0.1'}
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        data1 = response.json()
        subscribers = data1['data']['subscribers']
        return subscribers
    else:
        return 0


subreddit = "python3"
sub = number_of_subscribers(subreddit)
print(sub)
