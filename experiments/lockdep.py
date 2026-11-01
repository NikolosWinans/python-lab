#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.14"
# dependencies = [
#   "requests",
# ]
# ///

import requests

response = requests.get("https://httpbin.org/json")
print(response.json())