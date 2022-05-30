import socket

if __name__ == '__main__':
    # 1.创建tcp服务端套接字
    # AF_INET: ipv4, AF_INET6: ipv6
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 设置端口复用：服务器退出，端口号立即释放
    # 1.SOL_SOCKET：表示套接字
    # 2.SO_REUSEADDR：表示复用套接字的选项
    # 3.True：确定复用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)

    tcp_server_socket.bind(("", 8080))
    # 3.设置监听 128最大连接个数
    tcp_server_socket.listen(128)
    # 4.等待接收客户端的连接请求
    # 客户端跟服务端建立成功会返回一个套接字对象
    new_client, ip_port = tcp_server_socket.accept()
    print(new_client, ip_port)
    # 5.接收客户端程序
    while True:
        recv_data = new_client.recv(1024)
        print(recv_data.decode('gbk'))
        # 6.发送数据到客户端
        # 连接先由客户端断开
        send_content = input("请输入内容： ")
        new_client.send(send_content.encode('gbk'))
    new_client.close()
    # 7.关闭套接字
    tcp_server_socket.close()
