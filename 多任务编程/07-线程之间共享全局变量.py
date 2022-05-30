import threading
import time

flag = '这是全局变量'

def change():
    global flag
    flag = '被修改为了局部变量'

def read():
    print(flag)
if __name__ == '__main__':

    change_thread = threading.Thread(target=change)
    read_thread = threading.Thread(target=read)

    change_thread.start()
    # 因为线程的执行是无序的，下面这行的作用是让该线程执行完毕再继续主线程的
    change_thread.join()
    read_thread.start()
