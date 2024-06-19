#!/usr/bin/python3
"""This module defines the number_of_subscribers function"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    res = requests.get(url)
    if res.status_code != 200:
        return 0
    return res.json().get('data').get('subscribers')
