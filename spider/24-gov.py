

import requests
from lxml import etree
import jieba
from wordcloud import WordCloud
import time
from tqdm import tqdm
from tkinter import ttk
from tkinter import *
data = []

# primary_url = 'https://www.guizhou.gov.cn/zwgk/zfxxgk/yqlj/szzf/'
# secondary_url = 'https://www.guizhou.gov.cn/zwgk/zfxxgk/yqlj/xsqtqzf/'
# primary_rule = '//div[contains(@class,"zfxxgk_02Box")]//a/@title'
# secondary_rule = '//div[contains(@class,"zfxxgk_02Box")]//a/text()'
# url = 'https://www.guizhou.gov.cn/home/sxdt/index.html'
# rule = '//div[contains(@class,"PageMainBox")]//a/@title'
# def get_gov_name(url:str, rule:str)->list:
#     '''
#     根据指定的url和指定的xpath规则
#     :param url: 政府网址
#     :param rule: xpath规则
#     :return: 返回列表数据
#     '''
#     resp = requests.get(url=url)
#     resp.encoding = resp.apparent_encoding
#     html = etree.HTML(resp.text)
#     return html.xpath(rule)
# primary_list = get_gov_name(primary_url, primary_rule)
# primary_copy = [i[:-1] for i in primary_list]
# secondary_list = get_gov_name(secondary_url, secondary_rule)
# secondary_copy = [i[:-1] for i in secondary_list]
# all_gov = primary_list + primary_copy + secondary_list + secondary_copy
# print(primary_copy+secondary_copy)
# title_href_dict = {}
# def integrate_gov_data():
#     global data
#     for i in get_gov_name(url, rule):
#         if set(jieba.lcut(i)) & set(all_gov):
#             data += list(set(jieba.lcut(i)) & set(all_gov))
#     for i in range(1,51):
#         new_url = f'https://www.guizhou.gov.cn/home/sxdt/index_{i}.html'
#         for j in tqdm(get_gov_name(new_url, rule)):
#             if set(jieba.lcut(j)) & set(all_gov):
#                 data += list(set(jieba.lcut(j)) & set(all_gov))
#                 # sleep(0.1)

# def keep_in_txt():
#
# def draw_wordcloud():
#     global data
#     data = [i[:-1] if i[-1]=='市' or i[-1]=='州' or i[-1]=='县' or i[-1]=='区' else i for i in data]
#     w1 = WordCloud(font_path=r'C:\Windows\Fonts\STXINWEI.TTF',
#                    background_color='white',width=1600,height=800,max_words=len(all_gov)).generate(' '.join(data))
#     w1.to_file("gov.png")
#
# print(data)
#
# def main():
#     integrate_gov_data()
#     draw_wordcloud()
root = Tk()
def begin_month(event):
    date[1] = beginYear.get()
def finish_year(event):
    date[2] = finishYear.get()
def finish_month(event):
    date[3] = finishMon.get()
def begin_year(event):
    date[0] = beginYear.get()
def btn_click():
    print(date)
def begin_spider(str):
    print(date)
if __name__ == '__main__':


    # 时间变量声明
    beginYear = StringVar()
    beginMon = StringVar()
    finishYear = StringVar()
    finishMon = StringVar()
    date = [0,0,0,0]

    root.title('市州区县词频统计')
    height = root.winfo_screenheight()
    width = root.winfo_screenwidth()
    root.geometry(f'800x600+{(width-800)//2}+{(height-600)//2}')

    CurrentTimeLabel = Label(root,relief='raised', text=time.strftime("%Y-%m-%d"), foreground='green', font=("黑体",80),
                             image='::tk::icons::information',cursor='mouse',bitmap='hourglass',compound='left')
    box = ttk.Combobox(root, textvariable=beginYear,values=[str(i) for i in range(2015,2024)])
    box2 = ttk.Combobox(root, textvariable=beginMon,values=[str(i) for i in range(1,13)])
    box.bind("<<ComboboxSelected>>", begin_year)
    box2.bind("<<ComboboxSelected>>", begin_month)
    box3 = ttk.Combobox(root, textvariable=finishYear,values=[str(i) for i in range(2015,2024)])
    box4 = ttk.Combobox(root, textvariable=finishMon,values=[str(i) for i in range(1,13)])
    box3.bind("<<ComboboxSelected>>", finish_year)
    box4.bind("<<ComboboxSelected>>", finish_month)
    btn = Button(root,text='查询',command=btn_click)

    CurrentTimeLabel.pack()
    ttk.Separator(root).pack(fill="x", pady=5)  # 添加分割
    box.pack()
    box2.pack()
    ttk.Separator(root).pack(fill="x", pady=5)  # 添加分割
    box3.pack()
    box4.pack()
    btn.pack()

    print(beginYear.get())
    root.mainloop()

