from jieba.analyse import *
from wordcloud import WordCloud
import os
import pickle
# 解决中文乱码
cloud = WordCloud(font_path=r'C:\Windows\Fonts\STXINWEI.TTF')
AllWords = {}
if not os.path.exists('cloud'):
    os.mkdir('cloud')
def TF_IDF(data, index:int):
    global AllWords
    currentWord = {}
    for keyword, weight in extract_tags(data, topK=10, withWeight=True): # 输出10个关键词
        print(f"keyword is {keyword}, weight is {weight}")
        AllWords[keyword] = weight
        currentWord[keyword] = weight
        draw_wordcloud(cloud, currentWord, index)
def draw_wordcloud(cloud:WordCloud, data:dict, index:int):
    cloud.generate_from_frequencies(data)
    cloud.to_file(rf"cloud\第{index}个文本词云图.png")
with open('词向量抽取数据集.txt','r', encoding='u8') as f:   # 'r'是只读，a为覆盖，w为覆盖写入
    data = f.readlines() # 读取txt
    for index, value in enumerate(data):
        value = value.replace(r'\n','')
        value = value.replace(r'\xa0','')
        print(f"第{index+1}个文本的TF-IDF=======>")
        TF_IDF(value, index+1)
        print(value)
print(AllWords)
# 按照频次绘制关键字词云图
cloud.generate_from_frequencies(AllWords)
cloud.to_file("词云图.png")
print(f"在此文件夹下查看词云图:{os.getcwd()}")
# 序列化保存所有文本的关键词及其权重
with open('data.pickle','wb') as f:
    pickle.dump(AllWords,f,pickle.HIGHEST_PROTOCOL)
