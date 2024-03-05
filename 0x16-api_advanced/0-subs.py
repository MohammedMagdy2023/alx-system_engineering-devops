#!/usr/bin/python3
"""
    This script uses reddit api
"""
import requests


def number_of_subscribers(subreddit):
    """The function to use to return top10 posts of the subreddit"""
    headers = {'User-Agent': 'ALX_Student'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers)
    req_status = response.status_code
    req_headers = 'application/json; charset=UTF-8'

    if req_status == 200 and response.headers['content-type'] == req_headers:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
