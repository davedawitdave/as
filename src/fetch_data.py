# src/fetch_data.py

import requests


def fetch_data_from_kobotoolbox(api_url, headers):
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()
