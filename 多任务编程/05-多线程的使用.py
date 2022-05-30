import threading
# 线程之间的执行也是无序的
def sing():
    # 获取当前线程
    current_thread = threading.current_thread()
    print('sing : ',current_thread)
    for i in range(3):
        print('I am singing...')

if __name__ == '__main__':
    # 获取当前主线程
    current_thread = threading.current_thread()
    print('主线程： ',current_thread)
    sing_thread = threading.Thread(target=sing,name='sing')
    sing_thread.start()

