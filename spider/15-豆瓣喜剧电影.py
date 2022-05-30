import aiohttp
import asyncio
from lxml import etree
import requests
from time import sleep


url = 'https://movie.douban.com/j/chart/top_list'
headers = {
    'user-agent':'mozilla/5.0'
}
s = 0
title_list = []
rate_list = []
urls_list = []
director_list = []
release_time_list = []
running_time_list = []
params = {
    'type':'24',
    'interval_id':'100:90',
    'action':'',
    'start':s,
    'limit':'20'
}
def get_all_urls():
    '''
    该函数抓取前排行榜前560个数据
    :return: 详情页链接
    '''
    for s in range(0, 570, 20):
        main_page = requests.get(url=url, headers=headers, params=params)
        print(main_page.status_code)
        sleep(1)
        json_obj = main_page.json()
        for i in range(20):
            print(json_obj[i]['url'])
            urls_list.append(json_obj[i]['url'])

async def aio_get_detail_info(url):
    '''
    异步请求数据
    :return:
    '''
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, headers=headers) as resp:
            tree = etree.HTML(await resp.text(encoding='u8'))
            title_list.append(tree.xpath('//*[@id="content"]/h1/span[1]/text()')[0])
            rate_list.append(tree.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')[0])
            director_list.append(''.join(tree.xpath('//*[@id="info"]/span[1]/span[2]//text()')))
            release_time_list.append(tree.xpath('//*[@id="info"]/span[9]/text()')[0])
            running_time_list.append(tree.xpath('//*[@id="info"]/span[11]/text()')[0])

async def main():
    tasks = []
    for url in urls_list:
        tasks.append(aio_get_detail_info(url))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    get_all_urls()
    asyncio.run(main())



