from selenium.webdriver import Chrome
from time import sleep
driver = Chrome()
main_Mannufacture_Url = 'http://quote.eastmoney.com/center/boardlist.html?sortRule=1#boards-BK04651'
main_Industry_Url = 'http://quote.eastmoney.com/center/boardlist.html#boards2-90.BK0727'
industry_Name_List = []
industry_Closing_Price_List = []
industry_Quete_Change_List = []
industry_Number_List = []
mannufacture_Name_List = []
mannufacture_Closing_Price_List = []
mannufacture_Quete_Change_List = []
# 医疗行业 6
# 医疗制造 14  下一页 股票 收盘价 涨跌幅
driver.get(main_Mannufacture_Url)
# a = driver.find_element_by_xpath('//*[@id="table_wrapper-table"]/tbody/tr[1]/td[4]/a[2]')
# print(a.text)
tr_list = driver.find_elements_by_xpath('//*[@id="table_wrapper-table"]/tbody/tr')
for tr in tr_list:
    # tr.find_element_by_link_text()
    a_list = tr.find_elements_by_tag_name('a')
    industry_Number_List.append(a_list[0].text)
    industry_Name_List.append(a_list[1].text)
    a_list[3].click()
    driver.switch_to_window(driver.window_handles[-1])
    print(driver.page_source)
    break
exit(0)
while True:
    sleep(2)
    next_Page = driver.find_element_by_xpath('//*[@id="main-table_paginate"]/a[2]')
    # next_Page.click()