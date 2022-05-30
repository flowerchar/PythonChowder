import multiprocessing

main_valuable = '全局变量'

def change_valuable():
    global main_valuable
    main_valuable = '被函数修改了'

def print_valuable():
    print(f'print_valuable 的值是{main_valuable}')

if __name__ == '__main__':

    change_process = multiprocessing.Process(target=change_valuable)
    print_process = multiprocessing.Process(target=print_valuable)

    change_process.start()
    # 当前主进程等待上一个进程执行完毕再继续执行后面的进程
    # 这个可以有效保证：1.一个进程完全执行完才继续执行
    # 2.保证进程执行的无序性
    change_process.join()
    print_process.start()

    # 结论：进程之间不共享全局变量
    # 因为子进程获得的资源是拷贝主进程的