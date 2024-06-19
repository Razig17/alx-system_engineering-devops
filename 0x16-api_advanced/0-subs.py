#!/usr/bin/python3
"""This module defines the number_of_subscribers function"""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    res = requests.get(url, allow_redirects="false")
    subs = res.json().get('data')
    if subs:
        return subs.get('subscribers')
    return 0
