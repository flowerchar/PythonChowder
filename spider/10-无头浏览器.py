from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from time import sleep
import re

# 设置选项模式
opt = Options()
opt.add_argument('headless')
opt.add_argument('disable-gpu')

web = Chrome(options=opt)
sleep(2)
web.get('https://www.endata.com.cn/BoxOffice/index.html')
html_ = web.page_source
print(html_)
print('++++++++++++++++++')
# name_pat =  r'title="(?P<name>.*?)"'
# name_pat = r'<td style="width: 150px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: rgb\(16, 155, 238\);" title=".*?">(?P<name>.*?)<\td>'
name_pat = r'<td style="width: 150px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: rgb\(16, 155, 238\);" title="(.*?)">'
# name_res = re.finditer(name_pat, html_, re.I|re.S)
# for i in name_res:
#     print(i.group('name'))
# print(rangking_res)
name_res = re.finditer(name_pat, html_, re.I|re.S)
for i in name_res:
    print(i.group('name'))
a =r'<td style="width: 150px; white-space: nowrap; text-overflow: ellipsis; overflow: hidden; color: rgb\(16, 155, 238\);" title="(.*?)">'
title_first = re.findall(a, html_, re.S)
title = re.findall(r'<td style="width:150px; white-space:nowrap; text-overflow:ellipsis; overflow: hidden;" title="([^{].*?)">', html_, re.S)
# print(title)
# /html/body/div[5]/div/div/div[1]/div/div/table/tbody/tr[4]/td[2]