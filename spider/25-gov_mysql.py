import pymysql
import requests
from lxml import etree
import time
import jieba
from wordcloud import WordCloud
jieba.load_userdict('./mydict.txt')
TIME='2018-02_2022-03'
data = []
db = pymysql.connect(host='127.0.0.1',
                     user='root',
                     password='123456',
                     database='gov',
                     charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

primary_url = 'https://www.guizhou.gov.cn/zwgk/zfxxgk/yqlj/szzf/'
secondary_url = 'https://www.guizhou.gov.cn/zwgk/zfxxgk/yqlj/xsqtqzf/'
primary_rule = '//div[contains(@class,"zfxxgk_02Box")]//a/@title'
secondary_rule = '//div[contains(@class,"zfxxgk_02Box")]//a/text()'
url = 'https://www.guizhou.gov.cn/home/sxdt/index.html'
rule = '//div[contains(@class,"PageMainBox")]//a/@title'
def get_gov_name(url:str, rule:str)->list:
    resp = requests.get(url=url)
    resp.encoding = resp.apparent_encoding
    html = etree.HTML(resp.text)
    return html.xpath(rule)
primary_list = get_gov_name(primary_url, primary_rule)
primary_copy = [i[:-1] for i in primary_list]
secondary_list = get_gov_name(secondary_url, secondary_rule)
secondary_copy = [i[:-1] for i in secondary_list]
all_gov =  primary_copy + secondary_copy
print(all_gov)
def spider2():
    url = 'http://invest.guizhou.gov.cn/dtzx/gzdt/dfdt/index.html'
    rule = '//div[@class="NewsList"]//a'
    rule2 = '//div[@class="NewsList"]//li/span/text()'
    resp = requests.get(url=url)
    resp.encoding = resp.apparent_encoding
    html = etree.HTML(resp.text)
    a_s = html.xpath(rule)
    date_s = html.xpath(rule2)
    for i, j in zip(a_s, date_s):
        print([i.attrib.get('title'), i.attrib.get('href'), ''.join(j).strip()])
        data.append([i.attrib.get('title'), i.attrib.get('href'), ''.join(j).strip()])
    for i in range(1, 51):
        new_url = f'http://invest.guizhou.gov.cn/dtzx/gzdt/dfdt/index_{i}.html'
        new_resp = requests.get(new_url)
        new_resp.encoding = new_resp.apparent_encoding
        new_html = etree.HTML(new_resp.text)
        new_a_s = new_html.xpath(rule)
        new_date_s = new_html.xpath(rule2)
        for m, n in zip(new_a_s, new_date_s):
            data.append([m.attrib.get('title'), m.attrib.get('href'), ''.join(n).strip()])
            # time.sleep(0.1)
# spider2()
def spider():
    url = 'https://www.guizhou.gov.cn/home/sxdt/index.html'
    rule = '//div[contains(@class,"PageMainBox")]//a'
    rule2 = '//div[contains(@class,"PageMainBox")]//span/text()'
    resp = requests.get(url=url)
    resp.encoding = resp.apparent_encoding
    html = etree.HTML(resp.text)
    a_s = html.xpath(rule)
    date_s = html.xpath(rule2)
    for i, j in zip(a_s, date_s):
        data.append([i.attrib.get('title'), i.attrib.get('href'), ''.join(j).strip()])
    for i in range(1, 51):
        new_url = f'https://www.guizhou.gov.cn/home/sxdt/index_{i}.html'
        new_resp = requests.get(new_url)
        new_resp.encoding = new_resp.apparent_encoding
        new_html = etree.HTML(new_resp.text)
        new_a_s = new_html.xpath(rule)
        new_date_s = new_html.xpath(rule2)
        for m, n in zip(new_a_s, new_date_s):
            data.append([m.attrib.get('title'), m.attrib.get('href'), ''.join(n).strip()])
            time.sleep(0.1)


# spider()
print(data)

print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;")
def keep_in_mysql():
    for i in range(0,len(data)):
        print(str(data[i][0]),data[i][1],str(data[i][2]))
        sql = f"insert into gov(title,href,date) values ('{data[i][0]}','{data[i][1]}','{data[i][2]}');"

        # 运行sql语句
        cursor.execute(sql)
        # 修改
    db.commit()
        # 关闭游标
    cursor.close()
        # 关闭连接
    print("victory!", cursor.fetchall())
# 关闭数据库连接
    db.close()

def keep_in_mysql2():
    for i in range(0,len(all_gov)):
        print(all_gov[i])
        sql = f"insert into location(location) values ('{all_gov[i]}');"

        # 运行sql语句
        cursor.execute(sql)
        # 修改
    db.commit()
        # 关闭游标
    cursor.close()
        # 关闭连接
    print("victory!", type(cursor.fetchall()))
# 关闭数据库连接
    db.close()
words = []

def search_mysql(TIME):
    begin,finish = TIME.split('_')[0],TIME.split('_')[1]
    sql = f'select title, href from gov where DATE_FORMAT(date,"%Y-%m") >="{begin}" and DATE_FORMAT(date,"%Y-%m")<="{finish}";'
    cursor.execute(sql)
    db.commit()
    # cursor.close()
    # for i in cursor.fetchall():
    #     print(f'title is {i[0]}, href is {i[1]}')
    return cursor.fetchall()

def location_mysql()->dict:
    sql = 'SELECT location FROM location;'
    cursor.execute(sql)
    db.commit()

    words = []
    for i in cursor.fetchall():
        words.append(i[0])
    return dict(zip(words, [0 for i in range(0, len(words))]))
def jieba_process():
    text = ''
    for i in searchMysql:
        text += i[0]

    return jieba.lcut(text)

searchMysql = search_mysql(TIME)
text = jieba_process()
print(text)


locations:tuple = location_mysql()
# print(locations)
# ----
for i in text:
    for j in locations.keys():
        if j in i:
            locations[j] += 1
print(locations)
def draw_cloud(TIME):
    t = ''
    for i in locations:
        i *= locations[i]
        t += i
    # print('t is')
    # print(t)
    # print('jieba is')
    print(' '.join(jieba.lcut(t)))
    w1 = WordCloud(font_path=r'C:\Windows\Fonts\STXINWEI.TTF',
                       background_color='white',width=1600,height=800,collocations=False).generate(' '.join(jieba.lcut(t)))
    w1.to_file(f"{TIME}.png")
draw_cloud(TIME)
cursor.close()