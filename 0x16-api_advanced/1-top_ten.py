#!/usr/bin/python3
"""a function that queries the Reddit API and prints the
   titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    res = requests.get(url, headers={"User-Agent": "My-User-Agent"},
                       allow_redirects=False)
    if res.status_code >= 300:
        print('None')
        return
    for response in res.json()['data']['children']:
        print(response['data']['title'])
