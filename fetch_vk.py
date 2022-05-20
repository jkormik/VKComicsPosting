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


def save_vk_wall_photo(access_token, group_id, album_id, upload_url, user_id, file_name):
    with open('C:\\Users\\berry\\Desktop\\UrokiGit\\VKComicsPosting\\'+file_name, 'rb') as file:
        url = 'https://api.vk.com/method/photos.saveWallPhoto'
        payload = {
            'group_id': group_id,
            'album_id': album_id,
            'upload_url': upload_url,
            'user_id': user_id,
            'access_token': access_token,
            'v': '5.131'
        }
        files = {
            'photo': file
        }
        response = requests.post(url, params=payload, files=files)
        response.raise_for_status()
        decoded_response = response.json()
        if 'error' in response.json():
            raise requests.exceptions.HTTPError(decoded_response["error"])
    return decoded_response
