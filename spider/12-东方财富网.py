import requests
import json

url = "https://push2.eastmoney.com/api/qt/clist/get?cb=jQuery11230521405292206687_1617762504786&fid=f62&po=1&pz=50&pn=1&np=1&fltt=2&invt=2&ut=b2884a393a59ad64002292a3e90d46a5&fs=m%3A0%2Bt%3A6%2Bf%3A!2%2Cm%3A0%2Bt%3A13%2Bf%3A!2%2Cm%3A0%2Bt%3A80%2Bf%3A!2%2Cm%3A1%2Bt%3A2%2Bf%3A!2%2Cm%3A1%2Bt%3A23%2Bf%3A!2%2Cm%3A0%2Bt%3A7%2Bf%3A!2%2Cm%3A1%2Bt%3A3%2Bf%3A!2&fields=f12%2Cf14%2Cf2%2Cf3%2Cf62%2Cf184%2Cf66%2Cf69%2Cf72%2Cf75%2Cf78%2Cf81%2Cf84%2Cf87%2Cf204%2Cf205%2Cf124".encode('u8')
resp = requests.get(url=url)
resp.encoding = resp.apparent_encoding
getInfo = json.loads(resp.text[41:-2:])
each_info = getInfo['data']['diff']
for i in each_info:
    print(f'代码{i["f12"]} 名称{i["f14"]} 最新价{i["f2"]} 今日涨跌{i["f3"]}%')
# print('+'*10)
# print(resp.content)