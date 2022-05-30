from time import sleep
from selenium import webdriver
bro = webdriver.Chrome(executable_path='chromedriver.exe')
url = 'https://www.baidu.com/'
bro.get(url)
bro.find_element_by_xpath('//input[@id="kw"]').clear() # 1.该方法用于清理文本的内容
bro.find_element_by_xpath('//input[@id="kw"]').send_keys('iframe')   # 2.用于向里面输入文本信息
bro.find_element_by_xpath('//input[@id="su"]').click() # 3.提交表单，但是作用没有click()广泛
size = bro.find_element_by_xpath('//input[@id="kw"]').size # 4.搜索框（标签）的高度与宽度,text返回文本信息，get_attribute()返回属性值
print(size)



