import requests
from time import time
from hashlib import md5
import random


url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
headers = {
    # "Accept": "application/json, text/javascript, */*; q=0.01",
    # "Accept-Encoding": "gzip, deflate",
    # "Accept-Language": "zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7",
    # "Connection": "keep-alive",
    # "Content-Length": "241",
    # "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    # OUTFOX_SEARCH_USER_ID=1560157366@10.108.160.19; OUTFOX_SEARCH_USER_ID_NCOO=860414958.0648093; JSESSIONID=aaaeRrsMJuORvbdmXRnIx; ___rl__test__cookies=1617286203276
    "Cookie": "OUTFOX_SEARCH_USER_ID=1560157366@10.108.160.19; OUTFOX_SEARCH_USER_ID_NCOO=860414958.0648093; JSESSIONID=aaaLguLvozcpwg_bp6lIx; ___rl__test__cookies=1617257745084",
    # "Host": "fanyi.youdao.com",
    # "Origin": "http://fanyi.youdao.com",
    "Referer": "http://fanyi.youdao.com/", # @@@@@@@
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36", # @@@@@@@
    # "X-Requested-With": "XMLHttpRequest"
}
word = input("请输入你想要翻译的词语或者句子：")
currentTime = time()
secretTime = str(int(currentTime*1000))
salt = secretTime + str(random.randint(0,9))
# salt = secretTime
word_second = "fanyideskweb"+word+salt+"Tbh5E8=q6U3EXe+&L[4c@"
md = md5()
md.update(word_second.encode())
sign = md.hexdigest()
data = {
    "i": word,
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": salt,
    "sign": sign,
    "lts": secretTime,
    "bv": "77f6f59a0018c726a082dbc8637b193e",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_CLICKBUTTION"
}
resp = requests.post(url=url, headers=headers, data=data).json()
print(resp['translateResult'][0][0]['tgt'])
input('按下任意键继续...........')
