from time import sleep
import requests
import re
import csv
import os
from tqdm import tqdm

url = 'https://movie.douban.com/j/chart/top_list'
s = 0
title_list = []
rate_list = []
urls_list = []
director_list = []
release_time_list = []
running_time_list = []
headers = {
    'user-agent':'mozilla/5.0',
    # 'Cookie':'bid=lxcRRj0Pz2Y; ll="118371"; douban-fav-remind=1; __yadk_uid=B7Z3pj6OHTwdwCv25EzoGyff9eDFKItH; __gads=ID=2e3af4f26017506d-22a3c76b3cc5005d:T=1608189119:RT=1608189119:S=ALNI_MZKKt61zKHv38Jo98GkyQObYWzQbw; __utma=30149280.1123568305.1604162397.1604162397.1618493349.2; __utmz=30149280.1618493349.2.2.utmcsr=so.com|utmccn=(referral)|utmcmd=referral|utmcct=/link; __utmc=30149280; ap_v=0,6.0; push_doumail_num=0; push_noty_num=0; __utmv=30149280.20520; dbcl2="205207837:Krh34/3HSHs"; ck=3t0m; __utmt=1; __utmb=30149280.21.9.1618495164790; __utma=223695111.312895024.1618495197.1618495197.1618495197.1; __utmb=223695111.0.10.1618495197; __utmc=223695111; __utmz=223695111.1618495197.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1618495204%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; _pk_id.100001.4cf6=6acb99023bf55211.1618495204.1.1618495228.1618495204.'
    # 'Cookie': 'bid=zSCdnSwPuok; douban-fav-remind=1; __gads=ID=d999fa0a532eb43a-2290c01dc9c4004a:T=1605700304:RT=1605700304:S=ALNI_MYPHudGranWZo_Y-3xZ2f7cKAi6SQ; ll="118159"; _vwo_uuid_v2=DB6320A07054763A6C84A6DF9530A99EF|ed76fa7904978cd2a661a7bb89e32729; __yadk_uid=a0ypbX0yQs4YVsSDW5ySGCcAm4aLgadE; _vwo_uuid_v2=DB6320A07054763A6C84A6DF9530A99EF|ed76fa7904978cd2a661a7bb89e32729; push_noty_num=0; push_doumail_num=0; __utmv=30149280.22378; __utmz=30149280.1618411347.9.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=30149280.1507231615.1608467988.1618411347.1618458521.10; __utmc=30149280; __utmt=1; __utmb=30149280.2.10.1618458521; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1618458525%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=223695111.422592363.1608467988.1618412212.1618458525.10; __utmb=223695111.0.10.1618458525; __utmc=223695111; __utmz=223695111.1618458525.10.6.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_id.100001.4cf6=b423aa840f313f01.1608467987.9.1618458533.1618412246.; dbcl2="223780683:WeJcamod4qQ"; ck=MPKa'
    # 'Cookie':'bid=zSCdnSwPuok; douban-fav-remind=1; ll="118159"; _vwo_uuid_v2=DB6320A07054763A6C84A6DF9530A99EF|ed76fa7904978cd2a661a7bb89e32729; __yadk_uid=a0ypbX0yQs4YVsSDW5ySGCcAm4aLgadE; _vwo_uuid_v2=DB6320A07054763A6C84A6DF9530A99EF|ed76fa7904978cd2a661a7bb89e32729; push_noty_num=0; push_doumail_num=0; __utmv=30149280.22378; ct=y; __gads=ID=d999fa0a532eb43a-222822a370c70029:T=1618734158:RT=1618734158:S=ALNI_Mbmw11qOgSjlZPq9cDVNdd8K-g6bg; __utmc=30149280; __utmz=30149280.1618804384.23.11.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; dbcl2="223780683:P5lUelB4f1w"; ck=CqiE; __utmc=223695111; __utmz=223695111.1618804541.21.13.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1618819579%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.1507231615.1608467988.1618807784.1618819579.25; __utmb=30149280.0.10.1618819579; __utma=223695111.422592363.1608467988.1618807784.1618819579.23; __utmb=223695111.0.10.1618819579; _pk_id.100001.4cf6=b423aa840f313f01.1608467987.22.1618819606.1618807828.'
    # 'Cookie':'bid="MAdUPdhoK4o"; _vwo_uuid_v2=D806907560E6BE68B1EF0AD1515A7FBFB|e52474817cab06ffa81ba50e3cdea932; ll="118159"; douban-fav-remind=1; __gads=ID=b712280400c12532-226028c825c6005d:T=1614331214:RT=1614331214:S=ALNI_MYb9cFBiqJRwDOTczCciMtMiLl6sA; viewed="1029616"; gr_user_id=7e664313-52f5-4b49-ac39-f29f623c070a; __utmz=30149280.1614589564.4.2.utmcsr=so.com|utmccn=(referral)|utmcmd=referral|utmcct=/link; __utma=30149280.979437830.1588211646.1614589564.1618836775.5; __utmc=30149280; __utmt=1; dbcl2="236594605:nSnXvEFEUHA"; ck=IQJk; ap_v=0,6.0; push_noty_num=0; push_doumail_num=0; __utmv=30149280.23659; __utmb=30149280.4.10.1618836775; __utma=223695111.290178601.1618836904.1618836904.1618836904.1; __utmb=223695111.0.10.1618836904; __utmc=223695111; __utmz=223695111.1618836904.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1618836904%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __yadk_uid=AthDoNOf3Qfm53o2S0eWp9Nr7gcejx9f; _vwo_uuid_v2=D806907560E6BE68B1EF0AD1515A7FBFB|e52474817cab06ffa81ba50e3cdea932; _pk_id.100001.4cf6=f16c2fc245ddf165.1618836904.1.1618836909.1618836904.'
}
# proxies = {
#     'http':'http://47.104.92.49:4111/'
# }
title_pat = r'<span property="v:itemreviewed">(?P<title>.*?)</span>'
director_pat = r'rel="v:directedBy">(?P<director>.*?)</a>'
actor_pat = r'rel="v:starring">(?P<actor>.*?)</a>'
release_time_pat = r'<span property="v:initialReleaseDate" .*?>(?P<release_time>.*?)</span>'
running_time_pat = r'<span property="v:runtime" .*?>(?P<running_time>.*?)</span>'
rate_pat = r'property="v:average">(?P<rate>.*?)</strong>'
def get_all_urls():
    '''
    该函数抓取前排行榜前数据
    :return: 详情页链接
    '''
    for s in tqdm(range(0, 1000, 20)):
        params = {
            'type': '24',
            'interval_id': '100:90',
            'action': '',
            'start': s,
            'limit': '20'
        }
        main_page = requests.get(url=url, headers=headers, params=params, timeout=(60,7))
        try:
            # print(main_page.text)
            json_obj = main_page.json()
            # if json_obj['code']!=200:
            #     print('被识别为机器人程序，')
            # exit(-1)
            # print(json_obj)
        except TypeError:
            for i in main_page.text():
                urls_list.append(json_obj[i]['url'])
        except Exception as e:
            # print(main_page.text)
            print(e)
            exit(-1)
        for i in range(len(json_obj)):
            # print(json_obj[i]['url'])
            urls_list.append(json_obj[i]['url'])
        sleep(1)

def get_detail_info():
    '''
    向每个子链接发起请求，获得数据
    :return:
    '''
    for index,url in enumerate(tqdm(urls_list)):
            try:
                resp = requests.get(url=url, headers=headers, timeout=(60, 7))
                s = resp.text
                # print(s)
                title_list.append(re.search(title_pat, s).group('title'))
                director_list.append(re.findall(director_pat, s))
                release_time_list.append(re.findall(release_time_pat,s))
                running_time_list.append(re.findall(running_time_pat,s))
                rate_list.append(re.search(rate_pat, s).group('rate'))
            except Exception as e:
                print(f'第{index +1 }电影请求失败！',end='')
                print(e)
                continue
            sleep(10)

def keep_in_csv():
    '''
    以csv格式保存到本地
    :return:
    '''
    with open(f'douban_movie.csv',mode='w',encoding='u8',newline='') as fp:
        writer = csv.writer(fp)
        writer.writerow(['电影名称','电影片长','上映时间','导演','评分'])
        for i,j,k,l,m in zip(title_list,running_time_list,release_time_list,director_list,rate_list):
            writer.writerow([i,j,k,l,m])
    print(f'可以在此目录下查看文件{os.getcwd()}!')

if __name__ == '__main__':
    get_all_urls()
    get_detail_info()
    keep_in_csv()
