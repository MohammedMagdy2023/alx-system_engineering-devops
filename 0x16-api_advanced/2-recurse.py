#!/usr/bin/python3
"""
    This script uses reddit api
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """The function to use to return top10 posts of the subreddit"""
    headers = {'User-Agent': 'ALX_Student'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = '?limit=100&after={after}'
    response = requests.get(f'{url}+{params}', headers=headers)
    req_status = response.status_code
    req_headers = 'application/json; charset=UTF-8'

    if req_status == 200 and response.headers['content-type'] == req_headers:
        data = response.json()
        after = data['data']['after']
    if after is not None:
        for i in range(100):
            hot_list.append(data['data']['children'][i]['data']['title'])
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
