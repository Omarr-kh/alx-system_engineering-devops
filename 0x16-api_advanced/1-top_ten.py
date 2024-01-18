#!/usr/bin/python3
''' return top ten posts for a subreddit '''
import requests


def top_ten(subreddit):
    ''' function to return top 10 posts '''
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0 (by Omar)'}
    params = {'limit': 9}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data')
        hot_posts = data.get('children')

        for post in hot_posts:
            print(post['data']['title'])
    else:
        print(None)
