import os
import time


def learn_os():
    # 创建文件夹
    os.mkdir(r"D:\testDir")
    # 返回包含目录中文件名的列表
    print(os.listdir("./"))
    # 删除文件夹
    os.removedirs(r"D:\testDir")
    # 当前文件所在路径，不包含本文件名
    print(os.getcwd())
    # 判断路径是否存在
    if not os.path.exists("testDir"):
        os.mkdir("testDir")
    # 创建文件
    if not os.path.exists("testDir/test.txt"):
        f = open("testDir/test.txt", "w")
        f.write("hello world")
        f.close()


def learn_time():
    # 时间戳
    print(time.time())
    # 国外时间格式
    print(time.asctime())
    # 本地时间元素tuple
    print(time.localtime())
    # 设置时间格式
    print(time.strftime("%Y年%m月%d日 %H:%M:%S", time.localtime()))


if __name__ == '__main__':
    learn_time()
