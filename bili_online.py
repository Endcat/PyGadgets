import requests
from lxml import html

page = requests.get('https://www.bilibili.com/video/online.html')
tree = html.fromstring(page.content)

# 任意位置class=ebox的div节点
ebox_list = tree.xpath('//div[@class="ebox"]')

for ebox in ebox_list:
    title = ebox.xpath('.//a/p[@class="etitle"]/text()')[0].encode('ISO-8859-1').decode('utf-8')
    author = ebox.xpath('.//a[@class="author"]/text()')[0].encode('ISO-8859-1').decode('utf-8')
    online_num = ebox.xpath('.//p/b/text()')[0]
    url = "https:" + ebox.xpath('.//a/@href')[0]
    print("{} - {} - {} - {}".format(title, author, online_num, url))
