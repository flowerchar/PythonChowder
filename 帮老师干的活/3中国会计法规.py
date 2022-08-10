from tqdm import tqdm
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('blink-settings=imagesEnabled=false')

lost_list = []
print(f'在当前路径下操作{os.getcwd()}')
if not os.path.exists('./会计法规'):
    os.mkdir('./会计法规')
driver = webdriver.Chrome(executable_path=r'.\chromedriver.exe',options=chrome_options)
driver_detail = webdriver.Chrome(executable_path=r'.\chromedriver.exe',options=chrome_options)
for i in tqdm(range(1,5159)):#21
    base_url = f'http://law.esnai.com/do.aspx?controller=home&action=search&Efficiency=&order=&Business=&LawType=&DepartType=&Department=&trade=0&City1=000100000000&City2=&City3=&LawNo=&Fullindex=&Title=&EndDate=&StartDate=1900-1-1&page={i}'
    driver.get(base_url)
    print(base_url)
    lis = driver.find_elements_by_xpath('//*[@id="frm2"]/table[1]/tbody//a')
    for i in lis:
        directory = ''
        try:
            sleep(1)
            driver_detail.get(i.get_attribute('href'))
            a_list = driver_detail.find_elements_by_xpath(
                '/html/body/div[4]/table/tbody/tr/td[3]/table/tbody/tr/td/table[1]/tbody/tr/td/table/tbody/tr/td//a')
            for a in a_list:
                directory += a.text + '/'
            idContent = driver_detail.find_element_by_xpath('//*[@id="tdContent"]').text
            idTitle = driver_detail.find_element_by_xpath(
                '/html/body/div[4]/table/tbody/tr/td[3]/table/tbody/tr/td/table[2]/tbody/tr/td/table[2]/tbody/tr[1]/td[2]/b').text
            # print(idContent)
            wenhao = driver_detail.find_element_by_xpath(
                '/html/body/div[4]/table/tbody/tr/td[3]/table/tbody/tr/td/table[2]/tbody/tr/td/table[2]/tbody/tr[2]/td[2]').text
            bumen = driver_detail.find_element_by_xpath(
                '/html/body/div[4]/table/tbody/tr/td[3]/table/tbody/tr/td/table[2]/tbody/tr/td/table[2]/tbody/tr[3]/td[2]/a').text
            fawenTime = driver_detail.find_element_by_xpath(
                '/html/body/div[4]/table/tbody/tr/td[3]/table/tbody/tr/td/table[2]/tbody/tr/td/table[2]/tbody/tr[4]/td[2]').text
            shishiTime = driver_detail.find_element_by_xpath(
                '/html/body/div[4]/table/tbody/tr/td[3]/table/tbody/tr/td/table[2]/tbody/tr/td/table[2]/tbody/tr[5]/td[2]').text
            industry = driver_detail.find_element_by_xpath(
                '/html/body/div[4]/table/tbody/tr/td[3]/table/tbody/tr/td/table[2]/tbody/tr/td/table[2]/tbody/tr[7]/td[2]/a').text
            zone = driver_detail.find_element_by_xpath(
                '/html/body/div[4]/table/tbody/tr/td[3]/table/tbody/tr/td/table[2]/tbody/tr/td/table[2]/tbody/tr[8]/td[2]/a').text

            if wenhao == '':
                wenhao = '不存在'
            if bumen == '':
                bumen = '不存在'
            if fawenTime == '':
                fawenTime = '不存在'
            if shishiTime == '':
                shishiTime = '不存在'
            if industry == '':
                industry = '不存在'
            if zone == '':
                zone = '不存在'
            with open(f'./会计法规/{idTitle}.txt', 'w', encoding='gbk') as fp:
                fp.write(directory + '\n')
                fp.write(idTitle + '\n')
                fp.write(wenhao + '\n')
                fp.write(bumen + '\n')
                fp.write(fawenTime + '\n')
                fp.write(shishiTime + '\n')
                fp.write(industry + '\n')
                fp.write(zone + '\n')
                fp.write(idContent)
        except Exception as e:
            sleep(10)
            print(f"{i.get_attribute('href')}丢失！！信息：{e}")
            lost_list.append()
            with open("lost.txt","w") as fp:
                fp.write(lost_list)
            continue