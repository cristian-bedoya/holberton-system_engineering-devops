#!/usr/bin/python3
"""
Returns the number of subscribers (not active users, total subscribers)
for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """ Returns Number of subscribed """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    data_inf = requests.get(url, headers=headers, allow_redirects=False)

    if data_inf.status_code == 200:
        data = data_inf.json()['data']['children']
        for posts in data[:10]:
            print(posts['data']['title'])
    else:
        print(None)
