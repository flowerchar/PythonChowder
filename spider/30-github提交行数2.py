from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

new_list = []

a= ['StudyDataAnalysis', 'AutoGreen', 'SelectCourse', 'vue-ts-mp-shop', 'NAU-EIC', 'flowerchar', 'FullStack2', 'sky-take-out', 'sky-take-out-weixin', 'Vue3_Event_Admin', 'vue3_admin_template', 'Vue3Rabbit', 'StudyPygame', 'common_auth', 'PythonChowder', 'gov', 'example', 'StudyPython', 'JavaUtil', 'Take_Out', 'JavaWeb', 'test', 'full-stack_1', 'fun-rec', 'JavaProgramSummary', 'CProgramSummary', 'PrivateNotes', 'SpringbootTest', 'Hello-World', 'DeltaTrader', 'JavaGuide', 'Python-crawler-tutorial-starts-from-zero', 'snake', 'PyQt5', 'zju_cmooc']
b=['example','pythonGame','fun-rec', 'PrivateNotes','JavaGuide', 'Python-crawler-tutorial-starts-from-zero', 'snake', 'PyQt5', 'zju_cmooc']
d = webdriver.Chrome()

for i in set(a)-set(b):
    url = f'https://github.com/flowerchar/{i}/graphs/contributors'
    d.get(url)
    wait = WebDriverWait(d, 1000)
    element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="contributors"]/ol/li/span/h3/span[2]/span/div/span[1]')))
    num = d.find_element_by_xpath('//*[@id="contributors"]/ol/li/span/h3/span[2]/span/div/span[1]').text
    new_list.append(num)
    print(f"i --{i}--|| num is {num}")
print(new_list)

