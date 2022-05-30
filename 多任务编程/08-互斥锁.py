# 两个线程，每个线程都让全局变量加一，但是这样会产生错误
# 一个解决方法是.join()方法让主线程等待子进程结束
# 第二种是使用互斥锁
import threading
g_number = 0
lock = threading.Lock()
def add():
    lock.acquire()
    global g_number
    for i in range(100000):

        g_number +=1
    print('thread_1: ',g_number)
    lock.release()

def add_2():
    lock.acquire()
    global g_number
    for i in range(100000):

        g_number +=1
    print('thread_1: ', g_number)
    lock.release()
if __name__ == '__main__':

    thread_1 = threading.Thread(target=add)
    thread_2 = threading.Thread(target=add_2)

    thread_1.start()
    thread_2.start()

    print(g_number)