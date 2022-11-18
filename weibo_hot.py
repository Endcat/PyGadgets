from colorama import init
from colorama import Fore, Style
import requests
import json

def get_weibo_hot():
    url = "https://weibo.com/ajax/side/hotSearch"
    resp = requests.get(url)
    assert(resp.status_code == 200)
    hotlist = json.loads(resp.text)['data']
    # print(hotlist['realtime'][0])

    rank = 0
    prefix = "https://s.weibo.com/weibo?q="

    for card in hotlist['realtime']:
        rank = rank + 1
        hotword = "#"+card['note']+"#"
        # link = prefix + parse.quote(hotword)
        link = prefix + "%23"+ card['note'] +"%23"
        print(
                Fore.CYAN + str(rank) + Style.RESET_ALL +
                " - " + hotword +
                " - " + Style.DIM + link
            )

# for i in range(50):
#     index = i + 1
#     title = hotlist[i]['target']['title']

#     type = hotlist[i]['target']['type']
#     id = hotlist[i]['target']['id']

#     if type == 'question':
#         link = "https://zhihu.com/question/{}".format(id)
#     elif type == 'article':
#         link = "https://zhuanlan.zhihu.com/p/{}".format(id)

if __name__ == '__main__':
    init(autoreset=True)
    get_weibo_hot()
