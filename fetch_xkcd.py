import requests


def fetch_comics_xkcd_metadadata(url):
    response = requests.get(url)
    response.raise_for_status()
    decoded_response = response.json()
    if 'error' in response.json():
        raise requests.exceptions.HTTPError(decoded_response["error"])
    return decoded_response
