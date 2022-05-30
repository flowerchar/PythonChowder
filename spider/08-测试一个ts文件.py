import requests
import aiofiles

url = 'https://boba.52kuyun.com/20170906/Moh2l9zV/index.m3u8?sign=548ae366a075f0f9e7c76af215aa18e1'
resp = requests.get(url=url)
print(resp.text)
print('**'*10)
print(resp.content)
async with aiofiles.open('1.txt',mode='w',encoding='utf-8') as f:
    async for line in f:
        pass