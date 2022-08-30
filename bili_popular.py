# script for listing bilibili.com popular videos
# example get url:
# https://api.bilibili.com/x/web-interface/popular?ps=20&pn=1

import requests
import json

# 我只想查看前40个热门视频罢了，所以 20 * 2 = 40
count = 2

for i in range(count):
    url = "https://api.bilibili.com/x/web-interface/popular?ps=20&pn={}".format(str(i+1))
    response = requests.get(url)
    assert(response.status_code == 200)
    # print(json.dumps(response.text, indent=2, ensure_ascii=False))
    popular_list = json.loads(response.text)['data']['list']
    for j in range(20):
        category = popular_list[j]['tname']
        title = popular_list[j]['title']
        owner = popular_list[j]['owner']['name']
        # view = popular_list[j]['stat']['view']
        link = popular_list[j]['short_link']

        print("{} - {} - Up主：{} - {}".format(category, title, owner, link))