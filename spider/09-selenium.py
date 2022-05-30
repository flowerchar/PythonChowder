
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://yq2.nauvpn.cn/login')
sleep(11)
nextDontShow = driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/label')
nextDontShow.click()
hasRemenber = driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/label')
hasRemenber.click()
beginClick = driver.find_element_by_xpath('//*[@id="app"]/div/button')
beginClick.click()
account = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div/div[1]/div[2]/div/input')
account.send_keys('191091231')
password = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[2]/div/div[2]/div[2]/div/input')
password.send_keys('0037')
makeSure = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[3]/div[1]/span/label/span[1]')
makeSure.click()