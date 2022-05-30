from selenium import webdriver
from selenium.webdriver import ActionChains
from time import sleep
url='https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
#实例化一个谷歌驱动器
bro = webdriver.Chrome(executable_path='chromedriver.exe')
#找到一个url
bro.get(url)
#先定位到iframe框架
bro.switch_to.frame('iframeResult')
#找到要操作的标签
div = bro.find_element_by_id('draggable')
#实例化一个动作链，整个页面均为动作链对象
action = ActionChains(bro)
#执行动作链，缩小范围到div 1.点击并长按
action.click_and_hold(div)
#制造一个循环，模拟人类拖动
for i in range(5):
    action.move_by_offset(15,0).perform()
    sleep(1)
#释放动作链
action.release()
sleep(3)
#关闭驱动器
bro.quit()