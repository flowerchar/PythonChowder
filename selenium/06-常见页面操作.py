from time import sleep
from selenium import webdriver
bro = webdriver.Chrome(executable_path='chromedriver.exe')
# bro.set_window_size(640,80)  该方法用于设置浏览器尺寸
# bro.set_window_position(0,0) 该方法用于设置浏览器的绝对坐标
# bro.set_window_rect(0,0,640,80) 该方法相当于结合了上面两种
qq_url = 'https://qzone.qq.com/'
baidu_url = 'http://www.baidu.com'
bro.get(qq_url)
sleep(3) # 延迟三秒
bro.refresh() # 刷新页面
# bro.get(baidu_url)
# sleep(3)
# bro.back()  # 返回上一个网页
# sleep(2)
# bro.forward()  # 下一个网页

