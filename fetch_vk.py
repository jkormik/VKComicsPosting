import requests


def fetch_vk_groups(access_token):
    payload ={
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
    payload ={
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
