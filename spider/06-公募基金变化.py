import requests
from tqdm import tqdm
from time import sleep
url = 'http://www.szse.cn/api/market/ssjjhq/getTimeData?random=0.21160288370490088&marketId=1&code=399001'
resp = requests.get(url=url)
data = resp.json()
data = data['data']['picupdata']
for i in tqdm(data):
    print(i[1])
    sleep(1)
# datetime = data['datetime'][:-6:]
# data = data['data']['picupdata']
# def add_commma(ite:str) ->str:
#     '''
#     该函数作用是接收一个字符串，返回其按三位格式化后的
#     :param ite:
#     :return:
#     '''
#     s = ''
#     if '.' not in ite:
#         for index, value in enumerate(ite[::-1]):
#             if index % 3 == 0:
#                 s += ','
#                 s += value
#             else:
#                 s += value
#         return s[::-1][:-1:]
#     else:
#         former, middle, latter = ite.partition('.')
#         for index, value in enumerate(former[::-1]):
#             if index % 3 == 0:
#                 s += ','
#                 s += value
#             else:
#                 s += value
#         return s[::-1][:-1:] + middle +latter
# print(f'今日份日期是：{datetime}')
# for i in data:
#     print(f'当前时间[{i[0]}] 指数[{add_commma(str(i[1]))}] 涨跌[{i[2]}] 涨幅[{i[3]}%]',end='')
#     print(f' 成交量[{add_commma(str(i[4]))}手]',end='')
#     print(f' 成交额[{add_commma(str(i[5]))}元]', end='')
#     print()
# input('按下任意键继续...................')