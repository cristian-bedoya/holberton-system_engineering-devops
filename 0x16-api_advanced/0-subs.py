#!/usr/bin/python3
"""
Returns the number of subscribers (not active users, total subscribers)
for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """ Returns Number of subscribed """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    data_inf = requests.get(url, headers=headers, allow_redirects=False)
    if data_inf.status_code > 300:
        return 0
    data_inf = data_inf.json()
    return data_inf.get('data').get('subscribers')
