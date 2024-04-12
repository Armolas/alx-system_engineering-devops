#!/usr/bin/python3
"""This is the module to query a subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """returns the list of hot topics in a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    header = {'User-Agent': 'Armolas_pc'}
    params = {'after': after}
    response = requests.get(
            url,
            allow_redirects=False,
            headers=header,
            params=params
            )
    if response.status_code == 200:
        data = response.json()
        hots = data['data']['children']
        after = data['data']['after']
        for hot in hots:
            hot_list.append(hot['data']['title'])
        if after:
            return recurse(subreddit, hot_list=hot_list, after=after)
        else:
            return hot_list
    else:
        return None
