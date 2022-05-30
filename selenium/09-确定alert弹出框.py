from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
baidu_url='http://www.baidu.com'
driver = webdriver.Chrome()
driver.get(baidu_url)
link = driver.find_element_by_id('s-usersetting-top')
ActionChains(driver).move_to_element(link).perform()
driver.find_element_by_link_text('搜索设置').click()
sleep(0.5) # 这里一定一定要加一个延迟，不然页面还没刷新，浏览器无法找到标签
driver.find_element_by_link_text('保存设置').click()
# sleep(2)
driver.switch_to_alert().accept()