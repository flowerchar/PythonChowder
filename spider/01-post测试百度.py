import requests

url = 'https://www.baidu.com/'
headers = {
    'user-agent':'mozilla/5.0'
}
resp = requests.get(url=url)

resp.encoding = resp.apparent_encoding

print(resp.text)


print(resp.status_code)