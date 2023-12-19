from selenium import webdriver
from time import sleep
import csv
title_list, author_list, company_list = [], [], []
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://kns.cnki.net/knavi/journals/TXXB/detail?uniplatform=NZKPT')
sleep(5)
driver.find_element_by_xpath('//*[@id="2023_Year_Issue"]/dt/em').click()
sleep(2)


def extract_info():
    title_list.extend([element.text for element in
                 driver.find_elements_by_xpath("//*[@id='CataLogContent']//span[@class='name']/a")])
    author_list.extend([element.text for element in
                   driver.find_elements_by_xpath("//*[@id='CataLogContent']//span[@class='author']")])
    company_list.extend([element.text for element in
                    driver.find_elements_by_xpath("//*[@id='CataLogContent']//span[@class='company']")])

def keep_in_csv():
    header = ["title", "author", "company"]
    with open('output.csv', 'w', newline='', encoding='UTF-8') as csv_file:
        writer = csv.writer(csv_file)

        # 写入表头
        writer.writerow(header)
        # 同时迭代三个列表，写入数据行
        for data_row in zip(title_list, author_list, company_list):
            writer.writerow(data_row)

for i in ['10','09','08','07','06','05','04','03','02','01']:
    driver.find_element_by_xpath(f'//*[@id="yq2023{i}"]').click()
    sleep(5)
    extract_info()

keep_in_csv()