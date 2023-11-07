#!/usr/bin/python3
"""a recursive function that queries the Reddit API and returns
   a list containing the titles of all hot articles for a given subreddit.
   If no results are found for the given subreddit, the function should
   return None.
"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    res = requests.get(url, headers={"User-Agent": "My-User-Agent"},
                       params={'count': count, 'after': after},
                       allow_redirects=False)
    if res.status_code >= 400:
        return None
    for child in res.json()['data']['children']:
        hot_list = hot_list + [child['data']['title']]
    if not res.json()['data']['after']:
        return hot_list
    return recurse(subreddit, hot_list, res.json()['data'].get('count'),
                   res.json()['data']['after'])
