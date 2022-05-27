import requests


def fetch_xkcd_comics_metadadata(url):
    response = requests.get(url)
    response.raise_for_status()
    decoded_response = response.json()
    return decoded_response


def fetch_last_xkcd_comics_num():
    response = requests.get('https://xkcd.com/info.0.json')
    response.raise_for_status()
    decoded_response = response.json()
    return decoded_response['num']
