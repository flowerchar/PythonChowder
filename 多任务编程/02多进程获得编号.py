import multiprocessing
import os
import time
# 进程编号每次都不一样，不是固定的
def dance(name):
    dance_process_id = os.getpid()
    dance_process_main_id = os.getppid()
    print('跳舞进程的主进程是： ',dance_process_main_id)
    print('dance_process_id: ',dance_process_id)
    for i in range(3):
        print('I am {} ,I am dancing'.format(name))
        # 杀死进程：
        os.kill(dance_process_id,9)
        time.sleep(1)

def sing(name):
    sing_process_id = os.getpid()
    print('sing_process_id: ',sing_process_id)
    for i in range(3):
        print('I am {}, I am singing'.format(name))
        time.sleep(1)
if __name__ == '__main__':

    # 获取主进程的编号：
    main_process_id = os.getpid()
    print('main_process_id: ',main_process_id)
    main_main_process_id = os.getppid()
    print('主进程的主进程是：',main_main_process_id)
    dance_process = multiprocessing.Process(group=None,target=dance,args=('Billy',))#因为参数是以元组形式传递，所以要在最后加一个逗号，因为只有一个参数
    sing_process = multiprocessing.Process(group=None,target=sing,args=('Ketty',))
    # 子进程执行
    dance_process.start()
    sing_process.start()

