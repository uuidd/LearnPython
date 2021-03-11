"""
测试模块首先 import unittest
测试类必须继承 unittest.test.case
测试方法必须以"test_"开头
模块名字，类名没有特殊要求
setUp用来为测试准备环境，tearDown用来清理环境。
如果想要在所有case执行之前准备一次环境，并在所有case执行结束之后再清理环境，
我们可以用setUpClass()与 tearDownClass()；比如：数据库连接及销毁
如果想有些方法不在本次执行使用@unittest.skip测试方法的命名：以test开头
各种执行-单一用例，全部
"""
import os
import sys
import time
import unittest


class Demo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    def setUp(self) -> None:
        print("setUp")

    def tearDown(self) -> None:
        print("teardown")

    def test_case01(self):
        print("test_case01")
        self.assertEqual(2, 2, "不相等")

    def test_case02(self):
        print("test_case02")
        self.assertNotEqual("1", "2", "相等")

    @unittest.skipIf(1 + 1 == 2, "跳过这条用例")
    def test_case03(self):
        print("test_case03")


class Demo1(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    def setUp(self) -> None:
        print("setUp")

    def tearDown(self) -> None:
        print("teardown")

    def test_case01(self):
        print("test_case01")
        self.assertEqual(2, 2, "不相等")

    def test_case02(self):
        print("test_case02")
        self.assertNotEqual("1", "2", "相等")

    @unittest.skipIf(1 + 1 == 2, "跳过这条用例")
    def test_case03(self):
        print("test_case03")


if __name__ == '__main__':
    unittest.main()

if __name__ == "__main__":
    # 创建测试套件
    suites = unittest.TestSuite()
    # 自定义测试用例
    case_list = ['test_case01', 'test_case02', 'test_case03']
    for case in case_list:
        suites.addTest(Demo(case))

    # 运行测试用例，verbosity=2为每一个测试用例输出报告,run的参数是测试套件
    unittest.TextTestRunner(verbosity=2).run(suites)

if __name__ == '__main__':
    # 同时测试多个类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(Demo)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(Demo1)
    suite = unittest.TestSuite([suite1, suite2])
    unittest.TextTestRunner(verbosity=2).run(suite)
    sys.path.append(r"D:\MyDatabase\Code\Python\LearnPython\selenium_learn")
    # 报告路径
    report_path = os.path.join(os.path.dirname(__file__), 'report')
    now_time = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
    file_name = report_path + "/" + now_time + "_result.html"
    with open(file_name, 'wb') as fp:
        runner = HTMLTestRunner(
            stream=fp,
            time='测试报告',
            description='测试用例'
        )
        runner.run(suite)
if __name__ == '__main__':
    # 匹配所有以test开头的py文件，执行这些文件下所有的测试用例
    # discover可以一次调用多个脚本
    # test dir被测试脚本的路径
    # pattern脚本名称匹配规则
    test_dir = '../sxt'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")
