from selenium import webdriver

url = 'http://www.baidu.com'
PtrScr = 'C:\\Users\\DELL\\Desktop\\pictures\\'
begin_name = 'begin.png' # 只能是以.png结尾
end_name = 'end.png'
driver = webdriver.Chrome()
driver.get(url)
#color = input('请输入一个颜色： ')
js = ' var x=1;' # js代码
driver.get_screenshot_as_file(PtrScr+begin_name) # 截图并保存
driver.execute_script(js)  # 执行js代码
driver.get_screenshot_as_file(PtrScr+begin_name)
# import os
# print(os.getcwd())
# if os.path.exists(r'C:\Users\DELL\PycharmProjects\StageOne\selenium'):
#     print('True')
# else:
#     print('False')
