from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains # 需要执行一串动作，所以要导入一个动作链类
from selenium.webdriver.common.keys  import Keys
nau_url = 'https://www.nau.edu.cn/'
youxi_url = 'http://www.4399.com/'
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get(nau_url)
summary = driver.find_element_by_xpath('//*[@id="navi"]/div/div[1]/div/ul/li[1]/a')
# 实例化一个动作链对象，参数为驱动器
# 查看南审学校概况
# ActionChains(driver).double_click(summary).perform() # double_click()是双击，然后perform()是执行的意思
# context_click()是右击
# drag_and_drop(source,target)拖曳标签，source是起始标签，target是目的标签
driver.get(youxi_url)
# 向输入框输入洛克  王国
driver.find_element_by_id('smart_input').send_keys('洛克')
driver.find_element_by_id('smart_input').send_keys(Keys.SPACE*2) # 输入空格
driver.find_element_by_id('smart_input').send_keys('王国')
print(driver.title)
# 删除一个是send_keys(Keys.BACK_SPACE) 全选是send_keys(Keys.CONTROL,'a')，同理复制粘贴







