from socket import socket
from multiprocessing import Process


# 并发服务器
# 处理客户端的请求并为其服务
def deal_with_client(new_sock, dest_addr):
    while True:
        recv_data = new_sock.recv(1024)
        if len(recv_data) > 0:
            print("recv[%s]:%s" % (str(dest_addr), recv_data))
        else:
            print("[%s]客户端已经关闭" % str(dest_addr))
            break
    new_sock.close()


def main():
    ser_socket = socket(AF_INET, SOCK_STREAM)
    ser_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    local_addr = ("", 7788)
    ser_socket.bind(local_addr)
    ser_socket.listen(5)
    try:
        while True:
            print("主进程，等待新客户端到来")
            new_socket, dest_addr = ser_socket.accept()
            client = Process(target=deal_with_client, args=(new_socket, dest_addr))
            client.start()
            new_socket.close()
    finally:
        ser_socket.close()


if __name__ == '__main__':
    main()
