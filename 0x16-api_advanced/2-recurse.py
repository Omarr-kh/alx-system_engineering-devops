#!/usr/bin/python3
''' return a list containing the titles of
    all hot articles for a given subreddit.
'''
import requests


def recurse(subreddit, hot_list=[], after=None):
    ''' recursivly return hot articles of subreddit '''
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0 (by Omar)'}
    params = {'limit': 1,
              'after': after
              }

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None
    else:
        data = response.json().get(['data'])

        post = data['children'][0]
        hot_list.append(post['data']['title'])
        if len(data['children']) > 1:
            post = data['children'][1]
            hot_list.append(post['data']['title'])
        if data['after']:
            return recurse(subreddit, hot_list=hot_list, after=data['after'])
        else:
            return hot_list
