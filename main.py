import requests

OPENMIND_API_KEY = "<your_api_key_here>"
url = "https://api.openmind.org/some_endpoint"

headers = {"x-api-key": OPENMIND_API_KEY}

response = requests.get(url, headers=headers)
print(response.json())
