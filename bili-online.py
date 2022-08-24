from matplotlib.pyplot import title
import requests
from lxml import html

page = requests.get('https://www.bilibili.com/video/online.html')
tree = html.fromstring(page.content)

ebox_list = tree.xpath('//div[@class="ebox"]')

for ebox in ebox_list:
    title = ebox.xpath('.//a/p[@class="etitle"]/text()')[0].encode('ISO-8859-1').decode('utf-8')
    online_num = ebox.xpath('.//p/b/text()')[0]
    print(title," ",online_num)
