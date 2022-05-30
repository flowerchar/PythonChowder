import requests


url = 'https://www.baidu.com'
headers = {
    'user-agent':'mozilla/5.0'
}
# for i in range(1000):
resp = requests.get(url=url, headers=headers)
resp.encoding = resp.apparent_encoding
# print(resp.text)
print(resp.request.headers)