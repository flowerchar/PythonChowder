from selenium import webdriver

#from selenium.webdriver import ActionChains
from time import sleep
qq_url='https://qzone.qq.com/'
bro = webdriver.Chrome(executable_path='chromedriver.exe')
bro.get(qq_url)
bro.switch_to.frame('login_frame')
button = bro.find_element_by_id('switcher_plogin')
# action_1 = ActionChains(bro)
# action_1.click(button)
button.click()
user = bro.find_element_by_id('u')
password = bro.find_element_by_id('p')
user.send_keys('1941029880')
password.send_keys('*ptr77777')
submit = bro.find_element_by_id('login_button')
submit.click()
