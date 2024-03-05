#!/usr/bin/python3
"""
    This script uses reddit api
"""
import requests


def top_ten(subreddit):
    """The function to use to return top10 posts of the subreddit"""
    headers = {'User-Agent': 'ALX_Student'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    response = requests.get(url, headers=headers)
    req_status = response.status_code
    req_headers = 'application/json; charset=UTF-8'

    if req_status == 200 and response.headers['content-type'] == req_headers:
        data = response.json()
        for i in range(10):
            print(data['data']['children'][i]['data']['title'])
    else:
        return None
