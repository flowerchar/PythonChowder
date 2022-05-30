import numpy as np

salaryList = [5192,4422,4382,8234,6106,5173,5103,7451,7422,7238]
workingTimeList = [186,174,174,330,186,180,182,342,180,102]
d2kList = [6.25,0.25,2.25,1,2.25,0.25,9,1,12.25,36]

get_normal_data = lambda data:sum(data)/len(data)
def get_var2_data(data:list)->float:
    dataNormal = get_normal_data(data)
    totalSum = 0
    for i in data:
        totalSum += (i-dataNormal)**2
    return totalSum/(len(data)-1)

def get_cov_data(salaryList:list, workingTimeList:list)->float:
    salaryNormal = get_normal_data(salaryList)
    workingTimeNormal = get_normal_data(workingTimeList)
    totalSum = 0
    for i,j in zip(salaryList, workingTimeList):
        totalSum += (i-salaryNormal)*(j-workingTimeNormal)
    return totalSum/(len(salaryList)-1)

def get_r(salaryList:list, workingTimeList:list)->float:
    cov = get_cov_data(salaryList,workingTimeList)*(len(salaryList)-1)
    salaryNormal = get_normal_data(salaryList)
    workingTimeNormal = get_normal_data(workingTimeList)
    theta1, theta2 = 0, 0
    for i,j in zip(salaryList, workingTimeList):
        theta1 += (i-salaryNormal)**2
        theta2 += (j-workingTimeNormal)**2
    return cov/(theta1**0.5*theta2**0.5)

print(f"月薪的方差为{get_var2_data(salaryList)}，标准差{get_var2_data(salaryList)**0.5}，协方差为{get_cov_data(salaryList, workingTimeList)}，皮尔逊系数为{get_r(salaryList, workingTimeList)}")
print(f"工时的方差为{get_var2_data(workingTimeList)}，标准差{get_var2_data(workingTimeList)**0.5}，协方差为{get_cov_data(workingTimeList, salaryList)}，皮尔逊系数为{get_r(workingTimeList, salaryList)}")
print(f"以上是手写函数，以下是调用相应api，两种方法")
print(f"月薪的方差为{np.var(salaryList,ddof = 1)}，标准差{np.std(salaryList,ddof = 1)}，协方差为{np.cov(salaryList, workingTimeList)[0][1]}，皮尔逊系数为{np.corrcoef(salaryList, workingTimeList)[0][1]}")
print(f"工时的方差为{np.var(workingTimeList,ddof = 1)}，标准差{np.std(workingTimeList,ddof = 1)}，协方差为{np.cov(salaryList, workingTimeList)[0][1]}，皮尔逊系数为{np.corrcoef(salaryList, workingTimeList)[0][1]}")