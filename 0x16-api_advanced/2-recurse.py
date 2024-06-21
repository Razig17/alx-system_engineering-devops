#!/usr/bin/python3
"""This module defines the recurse function"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Print the title of the top 10 hot posts"""
    headers = {'User-Agent': 'Mozilla/5.0'}
    if after is not None:
        url = f'https://www.reddit.com/r/{subreddit}/top.json?after={after}'
    else:
        url = f'https://www.reddit.com/r/{subreddit}/top.json'
    res = requests.get(url, headers=headers)
    if (res.status_code == 200):
        top_posts = res.json()['data']['children']
        hot_list += [(post['data']['title']) for post in top_posts]
        next_page = res.json()['data']['after']
        if next_page is None:
            return hot_list
        return recurse(subreddit, hot_list, after=next_page)
    else:
        return None
