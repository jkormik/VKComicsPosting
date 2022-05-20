from dotenv import load_dotenv
from fetch_xkcd import fetch_comics_xkcd_metadadata
from fetch_vk import fetch_vk_groups, fetch_vk_wall_upload_server, save_vk_wall_photo
from data_collection import download_picture
import os


def main():
    load_dotenv()
    
    xkcd_comic_metadata = fetch_comics_xkcd_metadadata(
        'https://xkcd.com/info.0.json'
    )

    img_url = xkcd_comic_metadata['img']

    download_picture(
        img_url,
        'C:/Users/berry/Desktop/UrokiGit/VKComicsPosting'
    )
    file_name = img_url.rsplit('/', 1)[-1]
    print (file_name)

    vk_access_token = os.getenv('ACCESS_TOKEN')
    group_id = os.getenv('GROUP_ID')
    vk_server_data = fetch_vk_wall_upload_server(vk_access_token, group_id)
    album_id = abs(vk_server_data['response']['album_id'])
    upload_url = vk_server_data['response']['upload_url']
    user_id = vk_server_data['response']['user_id']
    print(save_vk_wall_photo(
        vk_access_token,
        group_id,
        album_id,
        upload_url,
        user_id,
        file_name
        )
    )


if __name__ == "__main__":
    main()
