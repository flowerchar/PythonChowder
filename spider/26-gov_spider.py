import requests
from lxml import etree
import jieba
from wordcloud import WordCloud
import time
from tqdm import tqdm
from tkinter import ttk
from tkinter import *
data = []
primary_url = 'https://www.guizhou.gov.cn/zwgk/zfxxgk/yqlj/szzf/'
secondary_url = 'https://www.guizhou.gov.cn/zwgk/zfxxgk/yqlj/xsqtqzf/'
primary_rule = '//div[contains(@class,"zfxxgk_02Box")]//a/@title'
secondary_rule = '//div[contains(@class,"zfxxgk_02Box")]//a/text()'
url = 'https://www.guizhou.gov.cn/home/sxdt/index.html'
rule = '//div[contains(@class,"PageMainBox")]//a/@title'
rule2 = '//div[contains(@class,"PageMainBox")]//i/text()'
def get_gov_name(url:str, rule:str)->list:
    '''
    根据指定的url和指定的xpath规则
    :param url: 政府网址
    :param rule: xpath规则
    :return: 返回列表数据
    '''
    resp = requests.get(url=url)
    resp.encoding = resp.apparent_encoding
    html = etree.HTML(resp.text)
    return html.xpath(rule)
primary_list = get_gov_name(primary_url, primary_rule)
primary_copy = [i[:-1] for i in primary_list]
secondary_list = get_gov_name(secondary_url, secondary_rule)
secondary_copy = [i[:-1] for i in secondary_list]
all_gov = primary_list + primary_copy + secondary_list + secondary_copy

title_href_dict = {}
def integrate_gov_data():
    global data
    for i in get_gov_name(url, rule):
        if set(jieba.lcut(i)) & set(all_gov):
            data += list(set(jieba.lcut(i)) & set(all_gov))
    for i in range(1,51):
        new_url = f'https://www.guizhou.gov.cn/home/sxdt/index_{i}.html'
        for j in tqdm(get_gov_name(new_url, rule)):
            if set(jieba.lcut(j)) & set(all_gov):
                data += list(set(jieba.lcut(j)) & set(all_gov))