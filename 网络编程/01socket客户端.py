import socket
if __name__ == '__main__':
    # 1.创建tcp套接字客户端编程
    # AF_INET:ipc4地址类型
    # SOCK_STREAM:tcp传输协议类型
    tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 客户端不要求设置端口号，也可设置
    # tcp_client_socket.bind(('',6666))
    # 2.和服务端套接字建立连接
    tcp_client_socket.connect(('10.213.88.35',8080))
    sent_content = 'hello this is pycharm'

    # 3.发送数据到服务端
    tcp_client_socket.send(sent_content.encode('gbk'))

    # 4.接收服务端的数据    1024为最大字节数
    receive_data = tcp_client_socket.recv(1024)
    print(receive_data.decode('gbk'))

    # 5.关闭套接字
    tcp_client_socket.close()