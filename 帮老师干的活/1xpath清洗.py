import csv
from lxml import etree
import os


def clear_text(path: str, i:str) -> list:
    parser = etree.HTMLParser(encoding="utf-8")
    path = path + '\\' + i
    print(path)
    html = etree.parse(path, parser=parser)

    raw_title = html.xpath(r'/html/body/div/p[1]/text()')
    raw_date = html.xpath(r'/html/body/div/p[3]/text()')
    raw_reading_times = html.xpath(r'/html/body/div/p[5]/text()')
    raw_text = html.xpath(r'/html/body/div/p[7]/text()')

    if path == path_3 + '\\' + i:
        raw_reading_times = html.xpath(r'/html/body/div/p[8]/text()')
    impurities = r'#a1{margin:25px140px;z-index:100;}@mediaalland(max-width:500px){#a1{width:100%!important;height:auto!important;margin:0auto;}#a1video{width:100%;height:auto;}#a1embed{width:100%;height:auto;}}'

    pure_title = ''.join("".join(raw_title).split())
    pure_date = ''.join("".join(raw_date).split())[1:-1:]
    pure_reading_times = ''.join("".join(raw_reading_times).split())[5::]
    pure_text = ''.join("".join(raw_text).split()).replace(impurities, '')

    if pure_title == '':
        pure_text = "None"
    if pure_date == '':
        pure_date = 'None'
    if pure_reading_times == '':
        pure_reading_times = 'None'
    if pure_text == '':
        pure_text = 'None'
    return [pure_title, pure_date, pure_reading_times, pure_text]


path_1 = ".\HTML\国家乡村振兴局 帮扶政策"
path_2 = ".\HTML\国家乡村振兴局 地方政策"
path_3 = ".\HTML\国家乡村振兴局 振兴要闻"
folders_1 = sorted(os.listdir(path_1), key=lambda x:int(x[13:-6]))
folders_2 = sorted(os.listdir(path_2), key=lambda x:int(x[13:-6]))
folders_3 = sorted(os.listdir(path_3), key=lambda x:int(x[13:-6]))

with open(f'{path_1[-4::]}.csv', 'w', encoding='utf-8', newline='\n') as fp:
    writer = csv.writer(fp)
    writer.writerow(['标题', '日期', '阅读次数', '正文'])
    for i in folders_1:
        writer.writerow(clear_text(path_1, i))
with open(f'{path_2[-4::]}.csv', 'w', encoding='utf-8', newline='\n') as fp:
    writer = csv.writer(fp)
    writer.writerow(['标题', '日期', '阅读次数', '正文'])
    for i in folders_2:
        writer.writerow(clear_text(path_2, i))
with open(f'{path_3[-4::]}.csv', 'w', encoding='utf-8', newline='\n') as fp:
    writer = csv.writer(fp)
    writer.writerow(['标题', '日期', '阅读次数', '正文'])
    for i in folders_3:
        writer.writerow(clear_text(path_3, i))
