from bilibili_api import Credential, sync
from bilibili_api.utils.network_httpx import request

import json

# follow the step to get credentials
# https://nemo2011.github.io/bilibili-api/#/get-credential

# 自己拿本地cookies 不要自己填了
cookies = chrome_cookies('https://www.bilibili.com')

sessdata = cookies['SESSDATA']
bili_jct = cookies['bili_jct']
buvid3 = cookies['buvid3']
dedeuserid = cookies['DedeUserID']

credential = Credential(sessdata=sessdata, bili_jct=bili_jct, buvid3=buvid3, dedeuserid=dedeuserid)

# example url
# https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/dynamic_new?uid={}&type_list=8
# https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/dynamic_history?uid={}&offset_dynamic_id={}&type=8

url_prefix = "https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr"

# 请求中的 type参数 有对应映射关系 详情参考bilibili-evolved
# @/components/feeds/api/types.ts -> feedsCardTypes
type = 8

def get_feed_response(is_history = False, history_offset = ""):
    if is_history:
        url = url_prefix + "/dynamic_history?uid={}&offset_dynamic_id={}&type={}".format(dedeuserid, history_offset, str(type))
    else:
        url = url_prefix + "/dynamic_new?uid={}&type_list={}".format(dedeuserid, str(type))

    response = sync(request("GET", url, credential=credential))
    return response

def print_feed_list(response):
    for card in response['cards']:
        card_info = json.loads(card['card'])
        owner = card_info['owner']['name']
        title = card_info['title']
        link = card_info['short_link']
        print("Up主：{} - {} - {}".format(owner, title, link))

# 默认打印前20 * 2个动态，也就是先请求一次new， 再请求一次history

response = get_feed_response()
history_offset = response['history_offset']
print_feed_list(response=response)

# 如果想要更多 就不停继续执行下面
count = 1

for i in range(count):
    response = get_feed_response(is_history=True, history_offset=history_offset)
    history_offset = response['next_offset']
    print_feed_list(response=response)
