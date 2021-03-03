from socket import *

# AF_INET表示ipv4，SOCK_DGRAM表示UDP
s = socket(AF_INET, SOCK_DGRAM)
# 以字节流方式发送数据
s.sendto("你好".encode("gb2312"), "192.168.1.13", 8082)

# 绑定固定接收端口
s.bind(('', 8788))
# 等待接收数据，最大为1024字节，阻塞
redata = s.recvfrom(1024)
redata[0].decode("gb2312") 
s.close()
