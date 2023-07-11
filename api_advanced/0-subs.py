#!/usr/bin/python3
"""Python script that returns the number of subscribers of a given subreddit"""

import requests


def number_of_subscribers(subreddit):
    """
    Get the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers.

    """
    # Create the API URL by formatting the subreddit
    api_url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set the user agent header
    headers = {"User-Agent": "My Bot/0.1"}

    # Send a GET request to the API
    response = requests.get(api_url, headers=headers)

    # Check if the response was successful
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()

        # Get the number of subscribers from the data
        subscribers = data["data"]["subscribers"]

        # Return the number of subscribers
        return subscribers
    else:
        # If the response was not successful, return 0
        return 0


subreddit = "python3"
sub = number_of_subscribers(subreddit)
print(sub)
