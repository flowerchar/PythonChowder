import requests


url = 'https://mooc1vod.stu.126.net/nos/mp4/2015/12/09/2610124_sd.mp4'
params = {
'ak': '7909bff134372bffca53cdc2c17adc27a4c38c6336120510aea1ae1790819de812008cd7fd3799dafcd09c4d0c4189f572834e20d76513d4207ac0a3ab08bc273059f726dc7bb86b92adbc3d5b34b1326035831eb7d550efdf947f1d436003c1'
}
headers = {
    'user-agent':'mozilla/5.0'
}
resp = requests.get(url=url, params=params, headers=headers)
print(resp.status_code)
with open('计组1.mp4',mode='wb') as fp:
    fp.write(resp.content)