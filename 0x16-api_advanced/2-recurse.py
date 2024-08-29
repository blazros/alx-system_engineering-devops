#!/usr/bin/python3
"""Module to query Reddit API recursively to get all hot post titles."""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively returns a list of titles of all hot posts for a given subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after, 'limit': 100}
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return None
        
        data = response.json().get('data', {})
        children = data.get('children', [])
        for post in children:
            hot_list.append(post.get('data', {}).get('title'))
        
        after = data.get('after')
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    except requests.RequestException:
        return None
