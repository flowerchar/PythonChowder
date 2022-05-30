from selenium import webdriver
driver = webdriver.Firefox(executable_path='geckodriver.exe')
driver.get(url='https://www.baidu.com')
driver.find_element_by_xpath('//*[@id="kw"]').send_keys('selenium文档')
driver.find_element_by_xpath('//*[@id="su"]').click()
