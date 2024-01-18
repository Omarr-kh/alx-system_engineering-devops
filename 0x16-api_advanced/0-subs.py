#!/usr/bin/python3
""" return number of subscribers for a subreddit """
import requests


def number_of_subscribers(subreddit):
    """ function to return number of subscribers """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {"User-Agent": "Mozilla/5.0 (Linux x86_64) Omar"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data")
        num_subscribers = data.get("subscribers")

        return num_subscribers
    else:
        return 0
