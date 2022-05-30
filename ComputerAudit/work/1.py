import pandas as pd

def getQ(getPos, data:pd.Series, indicator:float)->float:
    '''
    计算Q值
    :param getPos: 调用n+1或者n-1函数取得pos
    :param data: 源数据序列
    :param indicator: 几分位数
    :return: Q值
    '''
    Pos = getPos(data,indicator)
    fronter = int(Pos) - 1
    latter = int(Pos)
    return data[fronter]*indicator+data[latter]*(1-indicator)
getPosByPlus = lambda data,idx : (len(data)+1)*idx
getPosBySub = lambda data,idx : 1+(len(data)-1)*idx
data = pd.read_excel(r'../计算机审计实验数据/人力资源表.xlsx',sheet_name="薪水表")
min_salary = data["最低薪水"]
max_salary = data["最高薪水"]
print(f"n+1法下，{min_salary.name}Q1为{getQ(getPosByPlus, min_salary , 0.25)}")
print(f"n+1法下，{min_salary.name}Q2为{getQ(getPosByPlus, min_salary , 0.5)}")
print(f"n+1法下，{min_salary.name}Q3为{getQ(getPosByPlus, min_salary , 0.75)}")
print(f"n-1法下，{min_salary.name}Q1为{getQ(getPosBySub, min_salary , 0.25)}")
print(f"n-1法下，{min_salary.name}Q2为{getQ(getPosBySub, min_salary , 0.5)}")
print(f"n-1法下，{min_salary.name}Q3为{getQ(getPosBySub, min_salary , 0.75)}")
print(f"------------------------------------------")
print(f"n+1法下，{max_salary.name}Q1为{getQ(getPosByPlus, max_salary , 0.25)}")
print(f"n+1法下，{max_salary.name}Q2为{getQ(getPosByPlus, max_salary , 0.5)}")
print(f"n+1法下，{max_salary.name}Q3为{getQ(getPosByPlus, max_salary , 0.75)}")
print(f"n-1法下，{max_salary.name}Q1为{getQ(getPosBySub, max_salary , 0.25)}")
print(f"n-1法下，{max_salary.name}Q2为{getQ(getPosBySub, max_salary , 0.5)}")
print(f"n-1法下，{max_salary.name}Q3为{getQ(getPosBySub, max_salary , 0.75)}")