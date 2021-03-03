
# 单例模式
class MySingleton:

    __obj = None    # 类属性
    __init_flag = True    # 设置初始化值，让其只执行一次

    def __new__(cls, *arg, **kwargs):
        if cls.__obj == None:
            cls.__obj = object.__new__(cls)

        return cls.__obj

    def __init__(self, name):
        if MySingleton.__init_flag:
            print("init...")
            self.name = name
            MySingleton.__init_flag = False
    
a1 = MySingleton("a1")
a2 = MySingleton("a2")

print(a1)
print(a2)