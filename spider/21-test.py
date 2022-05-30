# from selenium import webdriver
# import requests
# from lxml import etree
#
# base_url = 'https://finance.sina.com.cn/roll/index.d.html?cid=249630&page=1'
# driver = webdriver.Chrome(executable_path=r'C:\Users\DELL\PycharmProjects\StageTwo\spider\chromedriver.exe')
# driver.get(base_url)
# lis = driver.find_elements_by_xpath("//div[@class='listBlk']//li//a")
# dates = driver.find_elements_by_xpath("//li")
# for i in lis:
#     print(i.text, i.get_attribute('href'))
# for li in lis:
#     driver.get(li.get_attribute('href'))#li.get_attribute('href')
#     # print(driver.page_source)
#     html = etree.HTML(driver.page_source)
#     article = ''.join(html.xpath('//*[@id="artibody"]//text()'))
#     print(article)
#     driver.back()
# import requests
#
# url = 'https://finance.sina.com.cn/jryx/bank/2022-03-09/doc-imcwipih7520941.shtml?finpagefr=p_115'
# resp = requests.get(url)
# resp.encoding = resp.apparent_encoding
# print(resp.text)s

s = ['asdas','dd']
print(s[0])