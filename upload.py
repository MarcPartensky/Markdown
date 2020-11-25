#!/usr/bin/env python

import sys
import os
import requests
import json

BASE_URL = os.environ['WEBSITE_URL']

path = sys.argv[1].replace('./', '')
file = path.split('/')[-1]

with open(path, 'r') as f:
    content = f.readlines()

content = '\n'.join(content[1:]).strip()
if content == '':
    raise Exception("This file is empty!")

url = f"{BASE_URL}/api/upload-markdown/"

raw_files = {'file': (file, content)}

response = requests.post(url, files=raw_files)
if response.status_code != 200:
    print(response)
else:
    print(f"{BASE_URL}/article/{file.replace('.md', '')}")
