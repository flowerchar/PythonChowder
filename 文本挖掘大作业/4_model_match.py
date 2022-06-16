#测试训练好的模型
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')# 忽略警告
import gensim
import pickle

if __name__ == '__main__':
    fdir = r'C:\Users\DELL\PycharmProjects\StageTwo\文本挖掘大作业'
    model = gensim.models.Word2Vec.load(fdir + '\wiki.zh.text.model')

    with open('data.pickle', 'rb') as f:  # 读入时同样需要指定为读取字节流模式
        data = pickle.load(f)
        # data有629个
    for index,i in enumerate(data):
        print(f"{index+1}.与{i}相似的十个词汇为：")
        try:
            word = model.wv.most_similar(i)
            for t in word:
                print(t[0],t[1])
        # 当词库没有该词语，跳过
        except KeyError:
            continue

