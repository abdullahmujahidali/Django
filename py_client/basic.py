import requests

# URL for the web service

endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.get(endpoint)
print(get_response.json())
