import requests
from lxml import etree
import os
from tqdm import tqdm

UTF_CHARSET = 'utf-8'
name_list = []
url_list = []
base_url = 'https://www.yingsx.com/'
url = 'https://www.yingsx.com/5_5731/'
resp = requests.get(url=url)
resp.encoding = UTF_CHARSET
html = etree.HTML(resp.text)
name_list = html.xpath('//*[@id="list"]/dl/dd/a/text()')
url_list = html.xpath('//*[@id="list"]/dl/dd/a/@href')
print(url_list)
if not os.path.exists('./完美世界'):
    os.mkdir('./完美世界')
for name, url_new in tqdm(zip(name_list, url_list)):
    with open(f'./完美世界/{name}.txt', 'w', encoding=UTF_CHARSET) as fp:
        resp1 = requests.get(url=base_url+url_new)
        resp1.encoding = UTF_CHARSET
        tree1 = etree.HTML(resp1.text)
        content = tree1.xpath('//*[@id="content"]/text()')
        fp.write(''.join(content))
print(f'可以在{os.getcwd()}下查看到文件')