from selenium import webdriver
import time
import unittest


class Common():
    '''
    简单封装
    '''
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def open_url(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(10)

    def close_driver(self):
        self.driver.quit()

    def go(self):
        com = Common()
        com.open_url("http://www.baidu.com")
        com.close_driver()

class Test1(unittest.TestCase):
    '''
    导入unittest测试用例类
    '''
    def setUp(self):
        '''
        每个测试用例开始前运行
        '''
        print("start")
    
    def tearDown(self):
        '''
        每个测试用例结束后运行
        '''
        print("stop")

    def test_001(self):
        print("001")

    def test_002(self):
        print("001")

    def test_003(self):
        print("003")

if __name__ == "__main__":
    # 运行测试用例的方法1，在测试用例类下的以test_开头的测试用例
    # unittest.main()
    
    # 运行测试用例的方法2
    # 创建测试套件
    suites = unittest.TestSuite()
    # 自定义测试用例
    case_list = ['test_001', 'test_002', 'test_003']
    for case in case_list:
        suites.addTest(Test1(case))
    # 运行测试用例，verbosity=2为每一个测试用例输出报告,run的参数是测试套件
    unittest.TextTestRunner(verbosity=2).run(suites) 
    