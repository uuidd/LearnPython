#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

print()
# list1 = [x for x in range(2, 11, 2)]
# print(list1)
# list2 = [x for x in range(1, 11) if x % 2 == 0]
# print(list2)
# list3 = [a + b for a in '123' for b in 'xyz']
# print(list3)
#
# g1 = (x for x in range(2, 100001, 2))
# print(type(g1))
#
# from collections import Iterable
#
# list4 = [1, 2, 3]
# for i in list1:
#     print(i)
# num = 100
# if isinstance(num, Iterable):
#     for i in num:
#         print(i)
# else:
#     print("num can't iterable")
#

# # 使用闭包，完成求两个数据和
# def func_out(num1):
#     def func_in(num2):
#         # 声明以下外部函数的变量
#         nonlocal num1
#         # 如果在内部函数中需要修改外部函数的变量，使用nonlocal声明
#         num1 += 1
#         return num2 + num1
#
#     return func_in
#
#
# a = 10
# b = 20
# f = func_out(a)
# print(type(f))
# result = f(b)
# print(result)
"""
 需求
     求两个点之间的距离

"""


# import math
#
#
# # 传统
# def get_dis(x1, x2, y1, y2):
#     return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
#
#
# # 闭包
# def get_dis_out(x1, y1):
#     def get_dis_in(x2, y2):
#         return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
#
#     return get_dis_in
# import time
#
#
# # 定义一个记录日志的函数：将访问事件以员访问的函载名与入到文件中(log.txt)
# def write_log(func):
#     try:
#         file = open('log.txt', 'a', encoding='utf-8')
#         # 写入相关数据信息（访问的函数名，访问的时间）
#         file.write(func.__name__)
#         file.write('\t')
#         # 写入访问时间
#         file.write(time.asctime())
#         file.write('\n')
#     except Exception as e:
#         print(e.args)
#     finally:
#         file.close()
#
#
# def func_out(func):
#     def func_in():
#         write_log(func)
#         func()
#
#     return func_in
#
#
# @func_out
# def func1():
#     print("功能1")
#
#
# @func_out
# def func2():
#     print("功能2")
#
#
# func1()
# func2()

# def func_out(func):
#     def func_in():
#         return '《' + func() + '》'
#
#     return func_in
#
#
# def func_out2(func):
#     def func_in():
#         return '$' + func() + '$'
#
#     return func_in
#
#
# @func_out2
# @func_out
# def book_name():
#     return '西游记'
#
#
# # book_name = func_out(book_name)
#
# print(book_name())
# def add_func():
#     print("新功能")
#
#
# def func_out(func):
#     def func_in(x, y):
#         add_func()
#         func(x, y)
#
#     return func_in
#
#
# @func_out
# def test(a, b):
#     print("a = %g b = %g" % (a, b))
#
#
# def func_out1(func):
#     def func_in(x, y, z):
#         add_func()
#         func(x, y, z)
#
#     return func_in
#
#
# @func_out1
# def test1(a, b, c):
#     print("a = %g b = %g c = %g" % (a, b, c))
#
#
# test(1, 2)
# test1(1, 2, 3)
# def func_out(func):
#     def func_in(*args, **kwargs):
#         print("新功能")
#         return func(*args, **kwargs)
#
#     return func_in
#
#
# @func_out
# def func0():
#     print("无参函数")
#
#
# @func_out
# def func1(a):
#     print("a = %g" % a)
#
#
# @func_out
# def func2(a, b):
#     print("a = %g b = %g" % (a, b))
#
#
# func0()
# func1(10)
# func2(20, 30)
# import types
#
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# def study(self):
#     print("学习使我快乐，一天不写代码，难受")
#
#
# p1 = Person("student1", 18)
# p2 = Person("student2", 20)
#
# p1.study = types.MethodType(study, p1)
# p1.study()
#
#
# # 添加静态方法
# @staticmethod
# def test_static_method():
#     print("我是静态方法")
#
#
# # 给类添加静态方法
# Person.method1 = test_static_method
# # 调用
# p1.method1()
# p2.method1()
# Person.method1()
#
#
# @classmethod
# def test_class_method(cls):
#     print("我是类方法")
#
#
# # 添加类方法
# Person.method2 = test_class_method
# # 对象访问
# p1.method2()
# p2.method2()
# # 类名访问
# Person.method2()
# 学习使我快乐，一天不写代码，难受
# 我是静态方法
# 我是静态方法
# 我是静态方法
# 我是类方法
# 我是类方法
# 我是类方法
# import types


# class Person:
#     __slots__ = ('name', 'age')
#
#     def __init__(self, new_name, new_age):
#         self.name = new_name
#         self.age = new_age
#
#
# def run(self):
#     print("run")
#
#
# zhangsan = Person("张三", 18)
# # zhangsan.addr = "北京" #AttributeError: 'Person' object has no attribute 'addr'
# zhangsan.run = types.MethodType(run, zhangsan) #AttributeError: 'Person' object has no attribute 'run'
# Person = type('Person', (), {})
# # p1 = Person()
# # print(p1)
# # print(Person.mro())
# # # <__main__.Person object at 0x0000027D076AA1F0>
# # # [<class '__main__.Person'>, <class 'object'>]

# class Animal:
#     def __init__(self, color):
#         self.color = color
#
#     def eat(self):
#         print("动物需要吃东西")
#
#
# def sleep(self):
#     print("狗狗趴着睡觉")
#
#
# Dog = type('Dog', (Animal,), {'age': 3, 'sleep': sleep})
# dog = Dog('Yellow')
# print(dog.age)
# dog.sleep()
# # 是否继承了父类中的特性
# print(dog.color)
# # 是否继承父类的方法
# dog.eat()
#
# print(Dog.__name__)

# class Test1:
#     def __init__(self, func):
#         self.__func = func
#
#     def __call__(self, *args, **kwargs):
#         print("在这可以实现新增任意功能")
#         self.add_func()
#         self.__func()
#
#     @staticmethod
#     def add_func():
#         print("用户权限验证")
#         print("日志系统处理")
#
#
# @Test1
# def test2():
#     print("我是功能2")
#
#
# test2()
# # 在这可以实现新增任意功能
# # 用户权限验证
# # 日志系统处理
# # 我是功能2
class AA:
    # 并创建对象开辟内存时调用
    def __new__(cls, *args, **kwargs):
        print("开辟内存空间")
        return super(AA, cls).__new__(cls)

    # 初始化方法
    def __init__(self):
        print("创建对象at：%s" % hex(id(self)))

    # 对象被系统回之前，会调用该方法
    def __del__(self):
        print("%s say bye bye" % hex(id(self)))


def test1(aaa):
    print(aaa)
    print("a的引用计数：%d" % sys.getrefcount(a))


a = AA()
print("a的引用计数：%d" % sys.getrefcount(a))
b = a
print("a的引用计数：%d" % sys.getrefcount(a))
list1 = [a]
print("a的引用计数：%d" % sys.getrefcount(a))
test1(a)
print("a的引用计数：%d" % sys.getrefcount(a))
print("*" * 50)

print("a的引用计数：%d" % sys.getrefcount(a))
list1.remove(a)
print("a的引用计数：%d" % sys.getrefcount(a))
del a
# 开辟内存空间
# 创建对象at：0x220be858580
# a的引用计数：2
# a的引用计数：3
# a的引用计数：4
# <__main__.AA object at 0x00000220BE858580>
# a的引用计数：7
# a的引用计数：4
# **************************************************
# a的引用计数：4
# a的引用计数：3
# 0x220be858580 say bye bye

