"""
进程，并行，十个进程同时进行，数据不共享，通过IPC通信方式共享信息
独立的地址空间、内存、数据栈
线程，并发，十个线程交互进行，共享信息，同步原语，锁
python使用全局解释器锁（GIL），只有一个主循环
原语，核心，多个线程会访问同一个数据，一定会造成错误
"""
import _thread
import logging
import threading
from time import sleep, ctime

# 初始化logging，打印info级别的日志
logging.basicConfig(level=logging.INFO)
"""
示例
"""
loops = [2, 4]


# 继承Thread类
class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    # 重写run方法
    def run(self):
        self.func(*self.args)


def loop(nloop, nesc):
    logging.info("start loop{0} at".format(nloop) + ctime())
    sleep(nesc)
    logging.info("end loop{0} at".format(nloop) + ctime())


def main():
    logging.info("start all at" + ctime())
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)
    for i in nloops:
        # 开启线程
        threads[i].start()
    for i in nloops:
        # 阻塞，等待线程执行完毕，避免使用锁机制
        threads[i].join()
    logging.info("end all at" + ctime())


"""
初接触
"""


def loop0():
    # ctime()当前时间
    logging.info("start loop0 at" + ctime())
    sleep(4)
    logging.info("end loop0 at" + ctime())


def loop1():
    logging.info("start loop1 at" + ctime())
    sleep(4)
    logging.info("end loop1 at" + ctime())


def main1():
    # _thread主线程杀掉时，子线程会被杀掉，没有守护线程
    logging.info("start all at" + ctime())
    _thread.start_new_thread(loop0, ())
    _thread.start_new_thread(loop1, ())
    sleep(6)
    logging.info("end all at" + ctime())


"""
新设计
"""


def loop3(nloop, nsec, lock):
    """

    :param nloop:用于标识当前loop是第几个
    :param nsec:时间
    :param lock:已经锁上的锁
    :return:
    """
    logging.info("start loop{0} at".format(nloop) + ctime())
    sleep(nsec)
    logging.info("end loop{0} at".format(nloop) + ctime())
    # 解开锁
    lock.release()


def main2():
    """
    等待每个线程执行结束后才结束
    :return:
    """
    logging.info("start all at" + ctime())
    locks = []
    nloops = range(len(loops))
    for _ in nloops:
        # 声明新的锁
        lock = _thread.allocate_lock()
        # 锁上锁
        lock.acquire()
        # 添加上所有的锁
        locks.append(lock)
    # 开启线程，没有添加在上面的原因是，加锁需要时间，锁没加上可能线程就执行完毕了
    for i in nloops:
        _thread.start_new_thread(loop3, (i, loops[i], locks[i]))
    for i in nloops:
        # 死循环判断，当锁上时不进行任何操作
        while locks[i].locked():
            pass
    logging.info("end all at" + ctime())


"""
全新设计
"""


def loop4(nloop, nesc):
    logging.info("start loop{0} at".format(nloop) + ctime())
    sleep(nesc)
    logging.info("end loop{0} at".format(nloop) + ctime())


def main3():
    logging.info("start all at" + ctime())
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = threading.Thread(target=loop4, args=(i, loops[i]))
        threads.append(t)
    for i in nloops:
        # 开启线程
        threads[i].start()
    for i in nloops:
        # 阻塞，等待线程执行完毕，避免使用锁机制
        threads[i].join()
    logging.info("end all at" + ctime())


if __name__ == '__main__':
    main()
