import socket
import time
import threading
"""
创建一个多线程的TCP服务器
接收来自客户端的消息，
然后将消息加上时间戳，并发送给客户端，
"""

def send_recv_fun(client_socket):
    """实现信息的收取、处理、和发送"""
    while True:
        recv_data = client_socket.recv(1024)
        if recv_data:
            send_data = "[%s]" % time.ctime() + recv_data.decode('gbk')
            client_socket.send(send_data.encode())
        else:
            print("...客户已断开连接..")
            break
    client_socket.close()


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.bind(('', 9999))
    tcp_server_socket.listen(128)
    while True:
        print("...等待客户连接...")
        #接收客户服务，创建客户套接字
        client_socket, client_address = tcp_server_socket.accept()
        print("...收到连接来自：%s" % str(client_address))
        #创建线程计划
        mt = threading.Thread(target=send_recv_fun, args=(client_socket,))
        #创建并执行子线程
        mt.start()

if __name__ == '__main__':
    main()