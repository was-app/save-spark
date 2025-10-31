import requests

def get(url, **kwargs):
    response = requests.get(url, timeout=10, **kwargs)
    response.raise_for_status()
    return response.json()

def post(url, **kwargs):
    response = requests.post(url, timeout=10, **kwargs)
    response.raise_for_status()
    return response.json()