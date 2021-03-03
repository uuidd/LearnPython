# TCP 服务器
# 三次握手，四次挥手不需要编写代码
# TCP服务器

from socket import *

# SOCK_STREAM表示TCP
tcp_sock = socket(AF_INET, SOCK_STREAM)
# ""空字符就就表示本机
tcp_sock.bind("", 7788)
# 最大连接数
tcp_sock.listen(5)
# 连接客户端，会返回新的sock端口，防止端口占用
new_sock, client_addr = tcp_sock.accept()
# 接收数据
data = new_sock.recv(1024)
# 发送数据，不需要指定地址
new_sock.send(b"xiexie")
new_sock.close()
# 关闭监听端口
tcp_sock.close()


# TCP客户端
from socket import *
client_sock = socket(AF_INET, SOCK_STREAM)
client_sock.connect(("192.168.1.17", 7788))
client_sock.send(b"nihao")
server_data = client_sock.recv(1024)
print(server_data)
client_sock.close()