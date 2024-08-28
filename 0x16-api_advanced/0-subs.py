#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    # Set a custom User-Agent to avoid being blocked by Reddit
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    # Make a GET request to the Reddit API
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the response is successful
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            # If the subreddit is invalid or not found, return 0
            return 0
    except requests.exceptions.RequestException:
        # Handle any request exceptions
        return 0
