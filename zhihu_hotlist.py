from urllib import response
from colorama import init
from colorama import Fore, Style
init(autoreset=True)

import requests
import json

url = "https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total?limit=50"
resp = requests.get(url)
assert(resp.status_code == 200)
hotlist = json.loads(resp.text)['data']

for i in range(50):
    index = i + 1
    title = hotlist[i]['target']['title']

    type = hotlist[i]['target']['type']
    id = hotlist[i]['target']['id']

    if type == 'question':
        link = "https://zhihu.com/question/{}".format(id)
    elif type == 'article':
        link = "https://zhuanlan.zhihu.com/p/{}".format(id)

    print(
            Fore.CYAN + str(index) + Style.RESET_ALL +
            " - " + title +
            " - " + Style.DIM + link
        )