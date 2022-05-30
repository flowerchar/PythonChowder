from selenium import webdriver
from time import sleep
bro=webdriver.Chrome(executable_path='./chromedriver.exe')
bro.get('https://www.taobao.com/')
search_input=bro.find_element_by_xpath('//input[@id="q"]')
get=input('请输入想搜索的东西')
search_input.send_keys(get)
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(2)
botton=bro.find_element_by_xpath('//div[@class="search-button"]/button')
botton.click()#//button[@class="btn-search"]
bro.get('https://www.baidu.com')
bro.back()
sleep(2)
bro.forward()
sleep(5)
