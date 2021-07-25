#!/usr/bin/env python
# -*- coding: utf-8 -*-

# print()
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
def func_out(func):
    def func_in(*args, **kwargs):
        print("新功能")
        return func(*args, **kwargs)

    return func_in


@func_out
def func0():
    print("无参函数")


@func_out
def func1(a):
    print("a = %g" % a)


@func_out
def func2(a, b):
    print("a = %g b = %g" % (a, b))


func0()
func1(10)
func2(20, 30)
