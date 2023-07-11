#!/usr/bin/python3
'''o-subs.py'''


import requests

# Get the number of subscribers of a subreddit
def number_of_subscribers(subreddit):
    api_url = f'https://www.reddit.com/r/{subreddit}/about.json'
    #used to set the user agent header
    headers = {'User-Agent': 'My Bot/0.1'}
    #send a GET request to the reddit api
    response = requests.get(api_url, headers=headers)
    #Used to check if the request was successful
    if response.status_code == 200:
        #parse the response to json
        data1 = response.json()
        #Get the number of subscribers
        subscribers = data1['data']['subscribers']
        # used to return the number of subscribers
        return subscribers
    else:
        #return 0 if the request was not successful
        return 0


subreddit = "python3"
sub = number_of_subscribers(subreddit)
print(sub)
