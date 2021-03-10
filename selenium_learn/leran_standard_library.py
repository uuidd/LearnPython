import os
import time
import urllib.request
import math


def get_all_paths(path):
    """
    获取文件夹中的所有文件
    """
    all_files = []
    if os.path.isdir(path):
        child_file = os.listdir(path)
        file_list = ["%s" % (path + os.path.sep + f) for f in child_file]
        while file_list is not None and len(file_list) > 0:
            all_files.append(file_list[0])
            if os.path.isdir(file_list[0]):
                child_file = os.listdir(file_list[0])
                if child_file is not None and len(child_file) > 0:
                    file_list = file_list + ["%s" % (file_list[0] + os.path.sep + f) for f in child_file]
                file_list.pop(0)
    else:
        print("找不到目录")


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


def learn_urllib():
    response = urllib.request.urlopen("http://www.baidu.com")
    # 状态码
    print(response.status)
    # 整个html页面
    print(response.read())
    # 头部信息
    print(response.headers)


def learn_math():
    # 返回大于等于的整数 6
    print(math.ceil(5.5))
    # 返回大于等于的整数 5
    print(math.floor(5.5))
    # 返回平方根
    print(math.sqrt(5))


if __name__ == '__main__':
    learn_math()
