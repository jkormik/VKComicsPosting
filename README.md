# VKontakte public comix posting 

The script is collecting random comicses from [xkcd JSON interface](https://xkcd.com/json.html) and posting them to VKontakte public.

### How to install

First of all you'll need to create **apllication** (standalone type is enough), get it's *client_id*. With *client_id* of your **application** you'll be able to get **access_token**. Also you will need to get *group_id*.

You can create **apllication** [here](https://vk.com/dev).

You can get **apllication** *client_id* [here](https://vk.com/apps?act=manage).
*client_id* looks something like this `1231231`.

To get **access_token** use Implicit Flow:
https://oauth.vk.com/authorize?client_id=*client_id*&display=page&scope=photos,groups,wall,offline&response_type=token&v=5.131&state=123456
**access_token** looks something like this `12h3gjgv213k123giu1bdjb1ug1g9g9gb08708wcn796918p28ucp1nn82mypx8y1pbyp10xmxmmxm9000xmx`. 
**access_token** should be assigned to `ACCESS_TOKEN` in `.env`.

You can get *group_id* [here](https://regvk.com/id/).
*group_id*  looks something like this `098765432`. 
*group_id*  should be assigned to `GROUP_ID` in `.env`.

Example of completed `.env` file.

```
ACCESS_TOKEN = '12h3gjgv213k123giu1bdjb1ug1g9g9g87yur8wcn796918p28ucp1nn82mypx8y1pbyp10xmxmmxm9000xmx'
GROUP_ID = '098765432'
```

Python3 should be already installed.
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### How to use

```
python main.py
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
