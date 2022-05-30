import requests
from lxml import etree
from selenium import webdriver
from tqdm import tqdm
words = ['人工智能', '区块链', '大数据', '互联网', '数字货币', '云计算', 'B2B']
AI = [[] for _ in range(18)]
BlockChain = [[] for _ in range(18)]
BigData = [[] for _ in range(18)]
IT = [[] for _ in range(18)]
Digit = [[] for _ in range(18)]
Cloud = [[] for _ in range(18)]
B2B = [[] for _ in range(18)]
years = [str(i) for i in range(2022, 2004, -1)]
def insert(s):
    print(s)
    index = 2022 - int(s)
    AI[index].append(article.count(words[0]))
    BlockChain[index].append(article.count(words[1]))
    BigData[index].append(article.count(words[2]))
    IT[index].append(article.count(words[3]))
    Digit[index].append(article.count(words[4]))
    Cloud[index].append(article.count(words[5]))
    B2B[index].append(article.count(words[6]))
driver = webdriver.Chrome(executable_path=r'C:\Users\DELL\PycharmProjects\StageTwo\spider\chromedriver.exe')
for j in tqdm(range(1,21)):
    base_url = f"https://finance.sina.com.cn/roll/index.d.html?cid=249630&page={j}"
    driver.get(base_url)
    lis = driver.find_elements_by_xpath("//li//a")
    # dates = driver.find_elements_by_xpath("//li")
    for li in lis:
        detial_url = li.get_attribute('href')
        year = detial_url.split('-')[0].split('/')[-1]
        resp = requests.get(detial_url)
        html = etree.HTML(resp.text)
        article = ''.join(html.xpath('//*[@id="artibody"]//text()'))
        # year = i.text.split('\n')[1][:4:]
        print(year, type(year))
        insert(year)
for i in years:
    print(f'{i}人工智能=={sum(AI[2022-int(i)])}, 区块链=={sum(BlockChain[2022-int(i)])}, 大数据=={sum(BigData[2022-int(i)])}, 互联网=={sum(IT[2022-int(i)])}, 数字货币=={sum(Digit[2022-int(i)])}, 云计算=={sum(Cloud[2022-int(i)])}, B2B=={sum(B2B[2022-int(i)])}')
