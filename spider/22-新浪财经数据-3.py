from selenium import webdriver
import csv
from lxml import etree
from tqdm import tqdm
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

words = ['人工智能', '区块链', '大数据', '互联网', '数字货币', '云计算', 'B2B']
AI = [[] for _ in range(2)]
BlockChain = [[] for _ in range(2)]
BigData = [[] for _ in range(2)]
IT = [[] for _ in range(2)]
Digit = [[] for _ in range(2)]
Cloud = [[] for _ in range(2)]
B2B = [[] for _ in range(2)]
years = [str(i) for i in range(2022, 2020, -1)]
def insert(s):
    index = 2022 - int(s)
    AI[index].append(article.count(words[0]))
    BlockChain[index].append(article.count(words[1]))
    BigData[index].append(article.count(words[2]))
    IT[index].append(article.count(words[3]))
    Digit[index].append(article.count(words[4]))
    Cloud[index].append(article.count(words[5]))
    B2B[index].append(article.count(words[6]))
all_detial_url = []
base_url = 'https://finance.sina.com.cn/roll/index.d.html?cid=249630&page=1'
driver = webdriver.Chrome(executable_path=r'C:\Users\DELL\PycharmProjects\StageTwo\spider\chromedriver.exe', options=chrome_options)
for i in range(1,21):#21
    base_url = f'https://finance.sina.com.cn/roll/index.d.html?cid=249630&page={i}'
    driver.get(base_url)
    lis = driver.find_elements_by_xpath("//div[@class='listBlk']//li//a")
    for i in lis:
        all_detial_url.append(i.get_attribute('href'))

for i in tqdm(all_detial_url):
    driver.get(i)
    html = etree.HTML(driver.page_source)
    date = str(html.xpath('//*[@id="top_bar"]//span[@class="date"]//text()')[0])[:4:]
    article = ''.join(html.xpath('//*[@id="artibody"]//p//text()'))
    insert(date)
with open("data2.csv", "w",encoding="utf-8", newline='\n') as fp:
    writer = csv.writer(fp)
    writer.writerow(["年份", *words])
    for i in years:
        writer.writerow([i, sum(AI[2022-int(i)]), sum(BlockChain[2022-int(i)]), sum(BigData[2022-int(i)]), sum(IT[2022-int(i)]), sum(Digit[2022-int(i)]), sum(Cloud[2022-int(i)]), sum(B2B[2022-int(i)])])
        print(f'{i}人工智能=={sum(AI[2022-int(i)])}, 区块链=={sum(BlockChain[2022-int(i)])}, 大数据=={sum(BigData[2022-int(i)])}, 互联网=={sum(IT[2022-int(i)])}, 数字货币=={sum(Digit[2022-int(i)])}, 云计算=={sum(Cloud[2022-int(i)])}, B2B=={sum(B2B[2022-int(i)])}')
    # print(AI)