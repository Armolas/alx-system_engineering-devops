#!/usr/bin/python3
"""This is the module to query a subreddit"""
import requests


def top_ten(subreddit):
    """returns the number of subscribers (not active users,
    total subscribers) for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    header = {'User-Agent': 'Armolas_pc'}
    response = requests.get(url, allow_redirects=False, headers=header)
    if response.status_code == 200:
        data = response.json()
        hots = data['data']['children']
        i = 0
        while i < 10:
            print(hots[i]['data']['title'])
            i += 1
    else:
        print(None)
