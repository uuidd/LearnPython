import pytest
import yaml

"""
场景:
    你与其他测试工程师合作一起开发时公共模块要在不同文件中要在大家都访问到的地方。
解决:
    contest.py这个文件进行数据共享，并且他可以放在不同位置起着不同的范围共享作用。
执行：
    系统执行到参数login时先从本文件中查找是否有这个名字的变量，之后在 contest.py中找是否有步骤
    将登陆模块带@pytest fixture写在 contest.py
contest py配置需要注意：
    contest文件名是不能换的
    contest.py与运行的用例要在同一个 package下，并且有__init__.py文件
    不需要 import导入conftset.py， pytest用例会自动查找
    全局的配置和前期工作都可以写在这里，放在某个包下，就是这个包数据共享的地方。
yield
    yield + 函数 == 生成器
    新建生成器p
    next(p)会一步一个值返回，不像return只能一次性返回
    相当于return + 暂停 + 记录上一次运行的位置
    在登陆的方法中加 yield，之后加销毁清除的步骤
    你已经可以将测试方法前要执行的或依赖的解决了，测试方法后销毁清除数据的要如何进行呢？

"""


@pytest.fixture(scope="module")
def login():
    print("第一次执行登录")
    yield
    print("第二次不执行登录")


@pytest.fixture(autouse=True)
def homepage():
    """
    每次都执行,autouse=True
    :return:
    """
    print("每次都执行这个")


def pytest_configure(config):
    """
    添加此模块pytest -s selenium_learn\\learn_pytest.py -m search
    才不会报错
    :param config:
    :return:
    """
    marker_list = ["search", "find"]
    for markers in marker_list:
        config.addinivalue_line(
            "markers", markers
        )


a = yaml.safe_load(open("data.yml"))
print(a)
