# API - Make a request
# Michi von Ah - Janaury 2024

import requests

endpoint = "https://example.com"

response = requests.get(endpoint)

print(response.text)