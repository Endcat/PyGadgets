from re import U
import requests
import json
from lxml import html
from colorama import init
from colorama import Fore, Style

# def get_bili_online():

#     page = requests.get('https://www.bilibili.com/video/online.html')
#     tree = html.fromstring(page.content)

#     # 任意位置class=ebox的div节点
#     ebox_list = tree.xpath('//div[@class="ebox"]')

#     for ebox in ebox_list:
#         title = ebox.xpath('.//a/p[@class="etitle"]/text()')[0].encode('ISO-8859-1').decode('utf-8')
#         author = ebox.xpath('.//a[@class="author"]/text()')[0].encode('ISO-8859-1').decode('utf-8')
#         online_num = ebox.xpath('.//p/b/text()')[0]
#         url = "https:" + ebox.xpath('.//a/@href')[0]
#         print(
#             Fore.CYAN + "Up主：" + author + Style.RESET_ALL +
#             " - " + title +
#             " - " + Fore.YELLOW + online_num + Style.RESET_ALL +
#             " - " + Style.DIM + url
#         )

def get_bili_online():
    url = "https://api.bilibili.com/x/web-interface/online/list"
    response = requests.get(url)
    assert(response.status_code == 200)
    online_list = json.loads(response.text)['data']
    # print(online_list)
    for card in online_list:
        owner = card['owner']['name']
        title = card['title']
        category = card['tname']
        online_count = card['online_count']
        link = card['short_link']
        # print(owner)
        print(
            Fore.CYAN + "Up主：" + owner + Style.RESET_ALL +
            " - " + title +
            " - " + Fore.YELLOW + category + Style.RESET_ALL +
            " - " + Style.DIM + link + Style.RESET_ALL +
            " - " + Style.DIM + str(online_count)
        )
if __name__ == '__main__':
    init(autoreset=True)
    get_bili_online()
