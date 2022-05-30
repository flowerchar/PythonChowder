import threading
import time

def sing():
    # 获取当前线程
    current_thread = threading.current_thread()
    print('sing : ',current_thread)
    for i in range(3):
        time.sleep(1)
        print('I am singing...')

if __name__ == '__main__':
    # 获取当前主线程
    current_thread = threading.current_thread()
    print('主线程： ',current_thread)
    # 解决办法是让子线程守护主线程
    # 方式一
    # sing_thread = threading.Thread(target=sing, name='sing',daemon=True)
    sing_thread = threading.Thread(target=sing,name='sing')
    # 方式二
    sing_thread.setDaemon(True)
    sing_thread.start()

    print('现在是主线程进行时')
    exit()


