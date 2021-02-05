#!/usr/bin/python3
"""
Returns the number of subscribers (not active users, total subscribers)
for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """ Returns Number of subscribed """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    data_inf = requests.get(url, headers=headers, allow_redirects=False)

    if data_inf.status_code > 300:
        print('None')

    for child in data_inf.json().get("data").get("children"):
        print(child.get("data").get("title"))
