from dotenv import load_dotenv
from fetch_xkcd import fetch_comics_xkcd_metadadata
from fetch_vk import fetch_vk_groups, fetch_vk_wall_upload_server
from data_collection import download_picture
import os


def main():
    load_dotenv()
    '''
    xkcd_comic_metadata = fetch_comics_xkcd_metadadata(
        'https://xkcd.com/info.0.json'
    )

    img_url = xkcd_comic_metadata['img']
    print(xkcd_comic_metadata['alt'])

    download_picture(
        img_url,
        'C:/Users/berry/Desktop/UrokiGit/VKComicsPosting'
    )
    '''

    vk_access_token = os.getenv('ACCESS_TOKEN')
    group_id = os.getenv('GROUP_ID')
    print(fetch_vk_wall_upload_server(vk_access_token, group_id))


if __name__ == "__main__":
    main()
