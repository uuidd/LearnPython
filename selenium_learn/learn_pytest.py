"""
笔记有些在conftest.py文件里
测试文件
    test_*.py
    *_test.py
用例识别
    Test*类包含的所有test_*的方法（测试类不能带有__init__方法）
    不在class中的所有的test_*方法
pytest可以执行 unittest框架写的用例和方法
终端
    pytest 文件名.py::类名::方法名
    pytest -x 文件名.py 一旦报错，立刻停止运行
    pytest -v 最高级别信息输出
    pytest -q 最简洁报告模式执行测试功能
    pytest -s 输出所有测试用的 print信息
    pytest -m 执行自定义标记的相关用例，结合@pytest.mask.标记名
断言失败也可继续执行
    pip install pytest-assume
    pytest.assume(1 == 4)
    pytest.assume(1 == 1)
setup,teardown，执行顺序
    1 模块级（setup_module/teardown_module）模块始末，全局的（优先最高）
    2 函数级（setup_function/teardown_function）只对函数用例生效（不在类中）
    3 类级（setup_class/teardown_class）只在类中前后运行一次（在类中）
    4 方法级（setup_method/teardown_method）开始于方法始末（在类中）
    5 类里面的（setup/teardown）运行在调用方法的前后
参数化使用，一一对应
    @pytest mark parametrize（argnames，argvalues）
    argnames：要参数化的变量，string（逗号分割），list，tuple
    argvalues：参数化的值，list，list[tuple]
yaml
    列表
        -
            1
            2
            3
    字典
        id:1
        name:2
        price:3
多线程并行与分布式执行
    pip3 install pytest-xdist
    多个CPU并行执行用例，直接加-n 3是并行数量：bytes -n 3
    在多个终端下一起执行
生成报告
    安装：
    pip install pytest-html
    生成html报告
    pytest -v -s --html-=report.html --self-contained-html
pytest.mark.run(order=1)，不推荐
    pip install pytest-order
    为测试用例设置顺序
pip freeze
    查看虚拟环境，环境依赖包有哪些
    导出
        pip freeze > requirements.txt
    安装
        pip install -r requirements.txt
pytest --setup-show
    查看每个用例fixture的调用顺序
作用域
    场景：范围是模块级别的。类似 setup Class
    解决：通过在同一模块中加入yield关键字，yield是调用第一次返回结果类似return，第二次执行它下面的语句返回。
    步骤：在@pytest fixture(scope="module"),module可以换成class，package，session
    注意，这种方式没有返回值，如果希望返回使用addfinalizer（终结器 ）
    把作用域设置成session就是全局了，全局可用
    不用 append到全局安量了更方便，fixture可以用来共享一些数
"""

# content of test_sample.p
import pytest
import yaml


def test_case1(login):
    """
    引入模块login，login这种共有模块存于conftest.py文件中，
    login加一个语法糖@pytest.fixture()
    :param login:
    :return:
    """
    print("case1, 需要登录")


def test_case2():
    print("case2, 不需要登录")


def test_case3(login):
    print("case3, 需要登录")


# 参数化，前两个变量，后面是对应的变量
@pytest.mark.parametrize("value, expected", [("3+5", 8), ("2+4", 6)])
def test_eval(value, expected):
    # eval 将字符串str当成有效的表达式来求值，并返回结果
    assert eval(value) == expected


# 参数化
@pytest.mark.parametrize("x", [1, 2])
@pytest.mark.parametrize("y", [1, 2, 3])
def test_xy(x, y):
    print("x={0}, y={1}".format(x, y))


test_user_data = ["Tome", "Jerry"]


@pytest.fixture(scope="module")
def login_r(request):
    user = request.param
    print(f"\n 打开首页准备登录，登录用户：{user}")
    return user


# indirect=Ture，可以把传过来的参数当函数来执行
@pytest.mark.parametrize("login_r", test_user_data, indirect=True)
def test_login(login_r):
    a = login_r
    print(f"login_r的返回值{a}")
    assert a != ""


# 跳过
@pytest.mark.skip("此次测试不执行")
def test_skip():
    print("执行")


# 有条件的跳过，根据不同平台跳过
@pytest.mark.skipif(1 == 1, reason="1等于1时跳过")
def test_skipif():
    print("执行")


# 跳过，未修复的错误
@pytest.mark.xfail
def test_fail():
    print("成功")


# search模块
# pytest -m search
# pytest -s selenium_learn\learn_pytest.py -m search
@pytest.mark.search
def test_search1():
    print("search1")
    pass


# search模块
@pytest.mark.search
def test_search2():
    print("search2")
    pass


# find模块
@pytest.mark.find
def test_find1():
    print("find1")


# find模块
@pytest.mark.find
def test_find2():
    print("find2")


@pytest.mark.parametrize(("a1", "b1"), yaml.safe_load(open("data.yml")))
def test_yaml(a1, b1):
    print(a1 + b1)


# @pytest.mark.parametrize("env", yaml.safe_load(open("./data.yml")))
# def test_yaml1(env):
#     if "test" in env:
#         print("测试环境的ip是：" + env["test"])
#     elif "dev" in env:
#         print("开发环境的ip是：" + env["dev"])


# 工厂模式，反向赋值，make_customer_record, test_cust_record
@pytest.fixture
def make_customer_record():
    def _make_customer_record(name):
        return {"name": name, "orders": []}

    return _make_customer_record


def test_customer_record(make_customer_record):
    customer1 = make_customer_record("Lisa")
    customer2 = make_customer_record("Mike")


if __name__ == '__main__':
    pytest.main("-v -x -s TestDemo")
    # pytest.main(["-v", "-s", "TestDemo"])
