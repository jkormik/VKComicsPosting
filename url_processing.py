from urllib.parse import unquote, urlsplit
import os.path


def get_file_name_from_url(url):
    splited_url = urlsplit(url)
    last_path_part = os.path.split(splited_url.path)
    return unquote(last_path_part[-1])
