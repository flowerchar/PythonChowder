import requests
import json
import re
from csv import writer
# 陇神戎发(300534) *ST金泰(600385)等等这些股票26号不存在交易记录
# pat_04_26 = '"2021-04-26.*?"'
pat_04_26 = f'"{input("请输入年份：")}-{input("请输入月份：")}-{input("请输入日期：")}.*?"'
manufacture_url = 'http://1.push2.eastmoney.com/api/qt/clist/get'
industry_url = 'http://24.push2.eastmoney.com/api/qt/clist/get'
zjlx_url = 'http://push2his.eastmoney.com/api/qt/stock/fflow/daykline/get'
un_checked_list = []
def get_zjlx(resp):
    '''
    根据Response，向该对象里的每一个条目发起股票详情页数据，获得04-26日交易数据
    :param resp: 接收一个页面js动态加载的公司列表json的Response对象
    :return:None
    '''
    js = json.loads(resp.text)
    for i in js['data']['diff']:
        stock_number = i['f12']
        stock_name = i['f14']
        sh_sz = i['f13']
        try:
            zjlx_params = {
                'fields1': 'f1,f2,f3,f7',
                'fields2': 'f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61,f62,f63,f64,f65',
                'secid': f'{sh_sz}.{stock_number}'
            }
            zjlx_resp = requests.get(url=zjlx_url, params=zjlx_params)
            s1 = re.findall(pat_04_26, zjlx_resp.text)[0]
            l1 = s1.split(',')
            csv_writer.writerow([str(stock_number),stock_name,l1[-4],l1[-3]])
            print(f'代码：{stock_number} |名称：{stock_name} |收盘价：{l1[-4]} |涨跌幅：{l1[-3]}%')
        except Exception as e:
            # print(e)
            un_checked_list.append([stock_name,stock_number])
            break
fp = open('04-26_data.csv', mode='w',encoding='u8',newline='')
csv_writer = writer(fp)
csv_writer.writerow(['股票代码','股票名称','21-04-26收盘价','21-04-26涨跌幅'])
print('医药制造2021-04-26的收盘价和涨跌幅')
for pn in range(1,15):
    params = {
        'pn':pn,
        'pz':'20',
        'po':'1',
        'np':'1',
        'fltt':'2',
        'invt':'2',
        'fid':'f3',
        'fs':'b:BK0465 f:!50',
    }
    resp = requests.get(url=manufacture_url,params=params)
    get_zjlx(resp)
print('='*20)
print('医疗行业2021-04-26的收盘价和涨跌幅')
for i in range(1,7):
    params = {
        'pn': i,
        'pz': '20',
        'po': '1',
        'np': '1',
        'ut': 'bd1d9ddb04089700cf9c27f6f7426281',
        'fltt': '2',
        'invt': '2',
        'fid': 'f3',
        'fs': 'b:BK0727 f:!50',
        'fields': 'f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152,f45'
    }
    resp = requests.get(url=industry_url,params=params)
    get_zjlx(resp)
csv_writer.writerow(['无效股票名称','股票代号'])
for invalid in un_checked_list:
    csv_writer.writerow(invalid)
fp.close()
print(f'2021-04-26日不存在交易记录的股票:{un_checked_list}')
