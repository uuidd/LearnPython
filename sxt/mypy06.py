# 手动添加全局变量__all__之后，from模块import * 将不在默认导入所有的功能，而是导入__all__列表中所包含的功能

__all__ = ['add', 'sub']

def add(a, b):
    """
    加法运算
    :return：两个数的和
    """
    return a + b

def sub(a, b):
    """
    减法运算
    :return：两个数的差
    """
    return a - b

import sys
paths = sys.path
for path in paths:
    print(path)

# 方法一
# 手动将模块添加到sys，path中
# 分隔符不要用“\”，用“/”或者“\\”，否则会报错
# 但是编写代码时无法使用，还是会显示错误
sys.path.append("D:/MyDatabase/Code/Python/LearnPython")

# 方法二
# 将模块所在路径，手动加入到sys.path中
# 将自定义模块，发布到系统目录
'''
    1.确定发布模块（目录结构）
    |--setup.py
    |--包
        |--模块
    2.编辑setup
        setup()
    3.构建模块
        python setup.py build
    4.发布模块
        python setup.py sdist
'''
# 新建setup.py
form distutils.core import setup
set(name = '自定义压缩包', version = '1.0', description = '描述', author = 'li', py_modules = ['package1.模块1', 'package1.模块2', 'package2.模块1'])

# 进入setup文件位置，cmd执行：python setup.py build
# 进入setup文件位置，cmd执行：python setup.py sdist

# 安装，找到刚才压缩包位置，解压文件，进入文件夹，cmd执行：python setup.py install，可以导入到系统库size-packages
# 暴力安装，直接将要安装的包以及模块，复制到对应的系统目录中，系统库size-packages  