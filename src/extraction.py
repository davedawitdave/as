# src/dataextraction.py

import requests
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def fetch_data_from_kobotoolbox(api_url, headers, limit=1000, offset=0):
    """Fetch data from KoboToolbox API with pagination."""
    data = []
    while True:
        params = {"limit": limit, "offset": offset}
        try:
            response = requests.get(api_url, headers=headers, params=params)
            response.raise_for_status()
            batch_data = response.json()["results"]
            data.extend(batch_data)
            logging.info(f"Retrieved {len(batch_data)} records, total: {len(data)}")
            if len(batch_data) < limit:
                break
            offset += limit
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
            break
        except Exception as err:
            logging.error(f"Other error occurred: {err}")
            break
    return data

# Example usage
if __name__ == "__main__":
    api_url = (
        "https://kf.kobotoolbox.org/api/v2/assets/aW9w8jHjn4Cj8SSQ5VcojK/data.json"
    )
    headers = {
        "Authorization": "Token f24b97a52f76779e97b0c10f80406af5e9590eaf",
        "Cookie": "django_language=en",
    }
    data = fetch_data_from_kobotoolbox(api_url, headers)
    print(f"Total records fetched: {len(data)}")
