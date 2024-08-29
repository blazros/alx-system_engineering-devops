#!/usr/bin/python3
"""Module to query Reddit API and count keywords in hot post titles."""

import requests


def count_words(subreddit, word_list, after=None, word_count=None):
    """Recursively counts keywords in hot post
    titles and prints sorted results."""
    if word_count is None:
        word_count = {}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after, 'limit': 100}
    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )
        if response.status_code != 200:
            return
        data = response.json().get('data', {})
        children = data.get('children', [])
        for post in children:
            title = post.get('data', {}).get('title', '').lower().split()
            for word in word_list:
                lower_word = word.lower()
                word_count[lower_word] = word_count.get(
                    lower_word, 0
                ) + title.count(lower_word)
        after = data.get('after')
        if after is not None:
            return count_words(subreddit, word_list, after, word_count)
        if word_count:
            sorted_words = sorted(
                word_count.items(), key=lambda kv: (-kv[1], kv[0])
            )
            for word, count in sorted_words:
                if count > 0:
                    print(f"{word}: {count}")
    except requests.RequestException:
        return
