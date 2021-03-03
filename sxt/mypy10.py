from socket import *
import struct

filename = 'dog.jpg'
server_ip = '192.168.1.17'
# pack后！表示以网络传输协议传输，后接格式，d表示一个数字字节，s表示文字字节，0为必要的分隔符
# 读写请求第一个1表示下载，2表示上传，5为操作码，前两个为操作码，后接文件名，0，模式，0
send_data = struct.pack('!H%dsb5sb'%len(filename), 1, filename.encode(), 0, 'octet'.encode(), 0)
s = socket(AF_INET, SOCK_DGRAM)
s.sendto(send_data, (server_ip, 69))
f = open(filename, 'ab')    # a表示以追加模式打开，b表示以二进制打开
while True:
    recv_data = s.recvfrom(1024)
    caozuoma, ack_num = struct.unpack('!HH', recv_data[0][:4])    # 获取操作码，ack
    rand_port = recv_data[1][1]    #获取服务器的随机端口
    if int(caozuoma) == 5:
        print('文件不存在。。。')
        break
    print("操作码：{0},ACK：{1},服务器端口：{2},数据长度：{3}".format(caozuoma, ack_num, rand_port, len(recv_data)))

    f.write(recv_data[0][4:])    # 写入数据
    if len(recv_data[0] < 516):
        break
    ack_data = struct.pack("!HH", 4, ack_num)
    s.sendto(ack_data, (server_ip, rand_port))   # 回复ACK确认包