#!/usr/bin/python3
"""Module to query Reddit API
and get the number of subscribers for a subreddit."""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit,
    or 0 if invalid."""
    try:
        url = f'https://www.reddit.com/r/{subreddit}/about.json'
        headers = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=headers, allow_redirects=False)
        if r.status_code == 200:
            return r.json().get('data', {}).get('subscribers', 0)
        return 0
    except requests.RequestException:
        return 0
