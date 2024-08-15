#!/usr/bin/python3
import requests
"""
Queries the Reddit API and returns
the number of subscribers for a given subreddit
"""


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    x = requests.get("https://www.reddit.com/r/{}/"
                     + "about.json".format(subreddit),
                     headers={"User-Agent": "Mozilla/5.0"})
    if x.status_code == 200:
        return x.json().get("data").get("subscribers")
    return 0
