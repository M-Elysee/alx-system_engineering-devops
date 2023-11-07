#!/usr/bin/python3
""" a recursive function that queries the Reddit API, parses the
    title of all hot articles, and prints a sorted count of given
    keywords (case-insensitive, delimited by spaces.
"""
import requests


def count_words(subreddit, word_list, count_dic={}, after=None):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    res = requests.get(url, headers={"User-Agent": "My-User-Agent"},
                       params={"after": after}, allow_redirects=False)
    if res.status_code != 200:
        return None

    hot_list = [c["data"]["title"] for c in res.json()["data"]["children"]]
    if not hot_list:
        return None

    word_list = list(dict.fromkeys(word_list))

    if count_dic == {}:
        count_dic = {word: 0 for word in word_list}

    for title in hot_list:
        split = title.split(' ')
        for word in word_list:
            for s in split:
                if s.lower() == word.lower():
                    count_dic[word] += 1

    if not res.json()["data"]["after"]:
        sorted_counts = sorted(count_dic.items(), key=lambda v: v[0])
        sorted_counts = sorted(count_dic.items(), key=lambda v: v[1],
                               reverse=True)
        [print('{}: {}'.format(k, v)) for k, v in sorted_counts if v != 0]
    else:
        return count_words(subreddit, word_list, count_dic,
                           res.json()["data"]["after"])
