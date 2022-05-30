import multiprocessing
import time
# multiprocessing.current_process()
# 获取当前进程的信息
def dance(name):
    for i in range(3):
        print('I am {} ,I am dancing'.format(name))
        time.sleep(1)

def sing(name):
    for i in range(3):
        print('I am {}, I am singing'.format(name))
        time.sleep(1)
#if __name__ == '__main__':

# 自己动手创建子进程
# group默认为None
# target是执行函数的名字
# args是按元组形式传参
# kwargs是按字典形式传参
# args和kwargs可以组合使用，要保证两个的并集就是目标函数的参数
start = time.time()
# 进程的执行是随机的
dance_process = multiprocessing.Process(group=None,target=dance,args=('Billy',))#因为参数是以元组形式传递，所以要在最后加一个逗号，因为只有一个参数
sing_process = multiprocessing.Process(group=None,target=sing,args=('Ketty',))
# 子进程执行
dance_process.start()
sing_process.start()
end = time.time()
print('总共用时{}'.format(end-start))