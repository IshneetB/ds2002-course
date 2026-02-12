#!/usr/bin/env python3

import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')

url = f'https://api.github.com/users/{GHUSER}/events'

response = requests.get(url)

data = json.loads(response.text)

for event in data[:5]:
    event_type = event['type']
    repo_name = event['repo']['name']
    print(event_type + " :: " + repo_name)