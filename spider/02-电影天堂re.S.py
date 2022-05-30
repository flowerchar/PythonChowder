import requests
import re

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

domain = 'https://www.dytt89.com/'
headers={
    'user-agent':'mozilla/5.0'
}
resp = requests.get(domain,verify=False, headers=headers)
resp.encoding = resp.apparent_encoding

obj1 = re.compile(r'2020必看热片.*?<ul>(?P<ul>.*?)</ul>', re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?>)'", re.S)

# result1 = obj1.finditer(resp.text)
# print(0)
# for it in result1:
#     ul = it.group('ul')
#     print(1)
#     result2 = obj2.finditer(ul)
#     for itt in result2:
#         print(2)
#         print(itt.group('href'))

print(resp.text)

# result1 = obj1.findall(string=resp.text)
# ul = result1[0]
# result2 = obj2.findall(string=ul)
# print(result2)
