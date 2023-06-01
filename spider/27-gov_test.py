import requests
from lxml import etree
url = 'https://www.guizhou.gov.cn/home/sxdt/index.html'
rule = '//div[contains(@class,"PageMainBox")]//a'
rule2 = '//div[contains(@class,"PageMainBox")]//span/text()'
resp = requests.get(url=url)
resp.encoding = resp.apparent_encoding
tree = etree.HTML(resp.text)
for i in tree.xpath(rule2):
    print(''.join(i).strip())
    # print()
# print()
