#!/usr/bin/python3
"""This module defines the top_ten function"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    res = requests.get(url, allow_redirects=False)
    if (res.status_code == 200):
        top_list = res.json()['data']['children']
        [print(post['data']['title']) for post in top_list]
    else:
        print(None)
