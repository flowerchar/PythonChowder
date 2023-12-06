import requests

url = "https://fanyi.baidu.com/sug"
keyword = {'kw':input("请输入想要翻译的词语：")}
print(requests.post(url=url, data=keyword).json()['data'][0])