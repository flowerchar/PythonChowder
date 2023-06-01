import requests
from lxml import etree
import os
from tqdm import tqdm
BASE_URL = "https://www.ibiquges.com/1/8345/"
URL = "https://www.ibiquges.com"
INVALID_LIST = ['\\','/',':','*','?','<','>','|']

def get_name_url_list():
    resp = requests.get(url=BASE_URL)
    tree = etree.HTML(resp.text)
    name_list = tree.xpath('//*[@id="list"]//a/text()')
    url_list = tree.xpath('//*[@id="list"]//a/@href')
    return name_list, url_list

def get_detail_info(name_list, url_list):
    invalid_var = 0
    if not os.path.exists('./完美世界小说合集'):
        os.mkdir('./完美世界小说合集')
    for name, url in tqdm(zip(name_list, url_list)):
        resp = requests.get(url=(URL+url))
        resp.encoding = resp.apparent_encoding
        tree = etree.HTML(resp.text)
        text_list = tree.xpath('//*[@id="content"]/text()')
        text = ''.join(text_list)
        for i in INVALID_LIST:
            if i in name:
                invalid_var += 1
                name = f'无效文件名{invalid_var}'
        with open(f'./完美世界小说合集/{name}.txt', mode='w', encoding='utf-8') as fp:
            fp.write(text)
    print(f'可以在{os.getcwd()}\完美世界小说合集目录下可以看到下载后的小说')

get_detail_info(*get_name_url_list())