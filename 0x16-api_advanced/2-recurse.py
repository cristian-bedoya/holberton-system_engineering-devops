#!/usr/bin/python3
"""
Returns the list of Hot comments for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], aft=""):
    """function that queries the Reddit API and returns
        a list containing the titles of all hot articles for a given subreddit
    """
    u = 'https://www.reddit.com/r/{}/hot/.json?after={}'.format(subreddit, aft)
    headers = {"User-Agent": "My-User-Agent"}
    response = requests.get(u, headers=headers)

    if response.status_code == 200:
        aft = response.json().get('data').get('children')

        for element in response.json().get('data').get('children'):
            hot_list.append(element.get('data').get('children'))

        if aft:
            recurse(subreddit, hot_list, aft)
        return hot_list
    return None
