import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
data = pd.read_excel(r"../计算机审计实验数据/支付明细表.xls")
pp = data.groupby("功能科目名称").agg({"支付金额":["sum"]})
pp.plot(y="支付金额",kind="pie")
plt.show()
