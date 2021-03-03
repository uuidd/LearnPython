# udp广播
# hub集线器广播，会出现广播风暴，计算机处理不了广播数据
# 交换机switch，会记录每台计算机的mac
# 路由器router，选择信息传输的线路，可以连接两个不同网段的交换机 
# 

from socket import *
dest = ("<broadcast>", 8080)
s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

# b表示以二进制
s.sendto(b"hi", dest)
while True:
    s.recvfrom()