import requests
import re
import os

# heroes_info_url = 'https://wjdown.99.com/games/cos/upload/yhzrheroattr/yhzr_hero_list.js?_=1615084782500'
# resp = requests.get(url=heroes_info_url)
# data = resp.json()
# for i in data:
#     print(f"{i['hero_id']},英雄编号")
#     # new_url = f"{i['headimg']}"[:-4:]+"0011"+f"{i['headimg']}"[-4::]
#     new_url = f'https://wjdown.99.com/games/cos/upload/yhzrheroheadimg/bg/{i["hero_id"]}0011.jpg'
#     print(new_url)
    # new_resp = requests.get(url=new_url).content
    # print(new_resp)
with open("aaa.jpg","wb") as fp:
    fp.write(requests.get(url="https://wjdown.99.com/games/cos/upload/yhzrheroheadimg/bg/1610010011.jpg").content)
# print(data)
# detail_hero_url_list = []
# detail_hero_name_list = []
#
# def get_hero_info():
#     '''
#     从英雄资料页面获得每一个英雄对应的图片链接和名字
#     :return:
#     '''
#     resp = requests.get(url=heroes_info_url)
#     # id值为4到六位的数字串
#     id_name_pat = r'"hero_id":"(?P<ID>\d{4,6}).*?"name":"(?P<name>.*?)"'
#     heroes_info = re.finditer(id_name_pat, resp.text)
#     print(heroes_info)
#     for i in heroes_info:
#         detail_hero_url_list.append(f'https://wjdown.99.com/games/cos/upload/yhzrheroheadimg/bg/{i.group("ID")}0011.jpg')
#         # 这里拿到的name是json字段的，需要转化格式
#         irregular_str = i.group('name')
#         china_char = eval(f'"{irregular_str}"')
#         detail_hero_name_list.append(china_char)
#
# def keep_in_file():
#     '''
#     向每个子页面发起请求，将图片下载保存下来
#     :return:
#     '''
#     if not os.path.exists('./英魂之刃图片合集'):
#         os.mkdir('./英魂之刃图片合集')
#     for url, name in zip(detail_hero_url_list, detail_hero_name_list):
#         img_data = requests.get(url=url).content
#         with open(f'./英魂之刃图片合集/{name}.{url.split(".")[-1]}', mode='wb') as fp:
#             fp.write(img_data)
#             print(f'{name}图片下载完成')
#     print(f'可以在{os.getcwd()}\英魂之刃图片合集目录下可以看到下载后的图片')
#
#
# if __name__ == '__main__':
#     get_hero_info()
#     keep_in_file()