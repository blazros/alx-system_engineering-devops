#!/usr/bin/python3
"""Module to query Reddit API and get the number of subscribers for a subreddit."""

import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit, or 0 if invalid."""
    try:
        r = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json',
                         headers={'User-Agent': 'Mozilla/5.0'}, allow_redirects=False)
        return r.json().get('data', {}).get('subscribers', 0) if r.status_code == 200 else 0
    except:
        return 0
