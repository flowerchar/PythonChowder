import requests
import execjs
import json

target_site = 'https://www.qimingpian.cn/finosda/project/pinvestment'

def request():
    url = 'https://vipapi.qimingpian.com/DataList/productListVip'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    }
    data = 'time_interval=&tag=&tag_type=&province=&lunci=&page=1&num=20&unionid='
    response = requests.post(url,headers=headers,data=data)
    print(response.json())
    # data = response.json()
    # return data

def decrypt_data():
    with open('js/企名片.js','r',encoding='utf8') as f:
        jscode = f.read()
    data = request()
    res = execjs.compile(jscode).call('o',data)
    print(json.loads(res))
# decrypt_data(
request()
decrypt_data()