from dotenv import load_dotenv
from fetch_xkcd import fetch_xkcd_comics_metadadata, fetch_last_xkcd_comics_num
from vk_integration import upload_photo_to_vk_server, \
    fetch_vk_wall_upload_server, save_vk_wall_photo, post_vk_wall
from data_collection import download_picture
import os
import random


def main():
    load_dotenv()

    random_xkcd_comics_number = \
        random.randint(1, fetch_last_xkcd_comics_num()+1)

    xkcd_comic_metadata = fetch_xkcd_comics_metadadata(
        f'https://xkcd.com/{random_xkcd_comics_number}/info.0.json'
    )

    img_url = xkcd_comic_metadata['img']

    download_picture(
        img_url,
        'C:/Users/berry/Desktop/UrokiGit/VKComicsPosting'
    )
    file_name = img_url.rsplit('/', 1)[-1]

    vk_access_token = os.getenv('ACCESS_TOKEN')
    group_id = os.getenv('GROUP_ID')
    vk_server_data = fetch_vk_wall_upload_server(vk_access_token, group_id)
    upload_url = vk_server_data['response']['upload_url']
    user_id = vk_server_data['response']['user_id']
    vk_server_answer = upload_photo_to_vk_server(upload_url, file_name)

    os.remove(file_name)

    save_vk_wall_response = save_vk_wall_photo(
        vk_access_token,
        user_id,
        group_id,
        vk_server_answer['photo'],
        vk_server_answer['server'],
        vk_server_answer['hash']
    )

    owner_id = f"-{group_id}"
    from_group = 1
    own_id = save_vk_wall_response['response'][0]['owner_id']
    media_id = save_vk_wall_response['response'][0]['id']
    attachments = f"photo{own_id}_{media_id}"
    message = xkcd_comic_metadata['alt']

    post_vk_wall(
        vk_access_token,
        owner_id,
        from_group,
        message,
        attachments
    )


if __name__ == "__main__":
    main()
