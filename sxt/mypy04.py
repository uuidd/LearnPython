class Student:
    # 方法没有重载，因为参数数量可变，而且没有数据类型

    # 类属性
    company = "XRG"

    # 
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # 析构方法
    def __del__(self):
        print("销毁对象{0}".format(self))

    # def __call__(self)相当于两小括号，pt_score()
    # 调用函数
    def pt_score(self):
        print("{0}的分数为{1}".format(self.name, self.score))

    # 类方法，操作类,默认参数cls指类当前对象 
    @classmethod
    def printCompany(cls):
        print(cls.company)

    # 静态方法，不需要自己
    # 类方法和静态方法中，不能调用实例变量、实例方法
    @staticmethod
    def add(a, b):
        print("{0}+{1}={2}".format(a, b, (a + b)))
        return a + b

    def go(self):
        s1 = Student("琼瑜", 100)
        s2 = Student("毅辉", 50)
        s1.pt_score()
        s2.pt_score()

        # 获取对象的所有属性、方法
        print(dir(Student))

        # 对象的字典
        print(s1.__dict__)

        print(isinstance(s1, Student))

        Student.add(20, 30)


# 方法的动态性
class Person:

    def work(self):
        print("努力上班！")

    def go(self):
        Person.play = play_game
        p1 = Person()
        p1.work()
        p1.play()

        Person.work = work2

        p1.work()


def play_game(who):
    print("{0}在玩游戏".format(who))


def work2(self):
    print("好好工作，努力上班！赚大钱，娶媳妇！")


class Employee:

    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 私有属性

    # 私有方法
    def __work(self):
        print("年龄：{0}".format(self.__age))

    def go(self):
        e1 = Employee("琼瑜", 18)

        print(e1._Employee__age)
        e1._Employee__work()


def go():
    e2 = Employee2("琼瑜", 10000)
    e2.set_salary(6000)
    print(e2.get_salary())


class Employee2:

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if 1000 < salary < 50000:
            self.__salary = salary
        else:
            print("录入错误，薪水应在1000-50000之间")


class Employee3:

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter  # 针对salary的设置
    def salary(self, salary):
        if 1000 < salary < 50000:
            self.__salary = salary
        else:
            print("录入错误，薪水应在1000-50000之间")

    def go(self):
        e3 = Employee3("琼瑜", 10000)
        e3.salary = 20000
        print(e3.salary)


# 多态
class Man:
    def eat(self):
        print("饿了，吃饭啦！")


class Chinese(Man):
    def eat(self):
        print("中国人用筷子吃饭")


class English(Man):
    def eat(self):
        print("英国人用筷子吃饭")


class Indian(Man):
    def eat(self):
        print("印度人用筷子吃饭")


def man_eat(m):
    if isinstance(m, Man):
        m.eat()
    else:
        print("不能吃饭")


def go():
    man_eat(Chinese())
    man_eat(Indian())
    man_eat(Man())


class Person1:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        if isinstance(other, Person1):
            return "{0}{1}".format(self.name, other.name)
        else:
            return "不是同类对象，不能相加"


p1 = Person1("相加")
p2 = Person1("向家")

print(p1 + p2)
