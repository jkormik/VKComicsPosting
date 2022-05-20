import requests


def fetch_vk_groups(access_token):
    payload = {
        'access_token': access_token,
        'v': '5.131'
    }
    response = requests.get('https://api.vk.com/method/groups.get', params=payload)
    response.raise_for_status()
    decoded_response = response.json()
    if 'error' in response.json():
        raise requests.exceptions.HTTPError(decoded_response["error"])
    return decoded_response


def fetch_vk_wall_upload_server(access_token, group_id):
    payload = {
        'group_id': group_id,
        'access_token': access_token,
        'v': '5.131'
    }
    response = requests.get('https://api.vk.com/method/photos.getWallUploadServer', params=payload)
    response.raise_for_status()
    decoded_response = response.json()
    if 'error' in response.json():
        raise requests.exceptions.HTTPError(decoded_response["error"])
    return decoded_response


def upload_photo_to_vk_server(upload_url, file_name):
    with open(file_name, 'rb') as file:
        files = {
            'photo': file
        }
        response = requests.post(upload_url, files=files)
        response.raise_for_status()
        decoded_response = response.json()
        if 'error' in response.json():
            raise requests.exceptions.HTTPError(decoded_response["error"])
    return decoded_response


def save_vk_wall_photo(access_token, user_id, group_id, photo, server, vk_hash):
    url = 'https://api.vk.com/method/photos.saveWallPhoto'
    payload = {
            'group_id': group_id,
            'user_id': user_id,
            'hash': vk_hash,
            'photo': photo,
            'server': server,
            'access_token': access_token,
            'v': '5.131'
    }
    response = requests.post(url, params=payload)
    response.raise_for_status()
    decoded_response = response.json()
    if 'error' in response.json():
        raise requests.exceptions.HTTPError(decoded_response["error"])
    return decoded_response
