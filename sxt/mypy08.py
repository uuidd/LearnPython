'''
简化私有属性的访问方式
@property
@属性.setter
'''

class Account():
    def __init__(self):
        self.__money = 0
    
    @property
    def money(self):
        return self.__money
    
    @money.setter
    def money(self, money):
        if isinstance(money, int):
            self.__money = money
        else:
            raise TypeError("金钱类型错误")
    
    def go(self):
        a1 = Account()
        a1.money = 100
        print(a1.money)

'''
多进程调用时是无序的
子进程之间不在同一存储空间，数据互不影响
'''

from multiprocessing import Process


def run1(name):
    print("12345%s"%(name))

def run2():
    print("555")

if __name__ == '__main__':
    # target指定函数名，不要加括号，args参数
    p1 = Process(target=run1, args=("test", ), name='进程1')    #位置参数
    p1.start()
    print(p1.name)
    print(p1.pid)
    # 等待子进程结束，主进程再结束，可以在里面填写超时时间
    p1.join()


    p2 = Process(target=run2)
    p2.start()
    p2.join()


from multiprocessing import Process
import time

class MyProcess(Process):
    def run(self):
        n = 5
        while n > 0:
            print(n)
            time.sleep(1)
            n -= 1

if __name__ == '__main__':
    p = MyProcess()
    p.start()
    p.join()


from multiprocessing import Pool
import time


def work(num):
    print(num)
    time.sleep(1)

if __name__ == '__main__':
    # 限制进程同时执行的进程数
    po = Pool()
    for i in range(20):
        # 用的少，用阻塞方式调用func
        po.apply(work, (i, ))
        # 不是用阻塞方式调用func，常用
        po.apply_async(work, (i, ))
    po.close()
    po.join()
    
