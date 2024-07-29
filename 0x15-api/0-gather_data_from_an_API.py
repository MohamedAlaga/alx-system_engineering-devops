 #!/usr/bin/python3
"""Gathers data from an API."""

import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user_id = sys.argv[1]
    user = requests.get("{}/users/{}".format(url, user_id)).json()
    todos = requests.get("{}/todos?userId={}".format(url, user_id)).json()

    completed = [task.get("title") for task in todos if task.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(task)) for task in completed]
