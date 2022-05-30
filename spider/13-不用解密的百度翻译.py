import requests


# url = 'https://fanyi.baidu.com/sug'
# data = {
#     "kw":input('请输入要翻译的：')
# }
# resp = requests.post(url=url,data=data)
# # print(resp.json()["data"])
# print(resp.json()["data"][0]["v"])

import requests


url = 'https://www.yingsx.com/5_5731/'
resp = requests.get(url=url)
resp.encoding = 'utf-8'
with open('ts1.txt', 'w') as fp:
    fp.write(resp.text)
print(resp.text)