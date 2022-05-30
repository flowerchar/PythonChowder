import multiprocessing
import time
# 主进程会等待所有子进程执行完毕才会结束
def test():
     #for i in range(10):
     while True:
        print('子进程仍在执行')
        time.sleep(0.2)

if __name__ == '__main__':
    # 两个方法会改变这种情况
    test_process = multiprocessing.Process(target=test)
    # 1.让子进程守护主进程，主进程结束销毁子进程，子进程依赖主进程
    # 2.让主进程退出之前先让子进程销毁
    # 1. 子进程守护主进程
    #test_process.daemon = True
    test_process.start()
    time.sleep(1)
    # 2.在主进程结束之前强制子进程销毁
    #test_process.terminate()
    print('子进程已经执行完毕')