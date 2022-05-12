from fetch_xkcd import fetch_comics_xkcd_metadadata
from data_collection import download_picture


def main():
    xkcd_comic_metadata = fetch_comics_xkcd_metadadata(
        'https://xkcd.com/info.0.json'
    )

    img_url = xkcd_comic_metadata['img']
    print(xkcd_comic_metadata['alt'])

    download_picture(
        img_url,
        'C:/Users/berry/Desktop/UrokiGit/VKComicsPosting'
    )


if __name__ == "__main__":
    main()
