#!/usr/bin/python3
""" return number of subscribers for a subreddit """
import requests


def number_of_subscribers(subreddit):
    """ function to return number of subscribers """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    url_header = {"user-agent": "request"}
    response = requests.get(url, headers=url_header, allow_redirects=False)

    if response.status_code != 200:
        return 0
    data = response.json().get("data")
    num_subscribers = data.get("subscribers")

    return num_subscribers
