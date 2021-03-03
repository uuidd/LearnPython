#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
此文件为特别注释版，每一行的空行都有规范，并非没有作用，请注意，例如import后要空三行，return前空一行
请注意此文件的变量、类、函数命名方式，类每个单词首字母大写，文件名、函数、变量小写单词用_隔开
'''

import math



class CalculateDistance1():
    '''
    CalculateDistance：计算距离，使用列表的方式存值
    '''
    def in_xy(self):
        '''
        输入两点的浮点数坐标，并返回两个坐标的列表
        '''
        '''
        此处注释是给你特别注解的，正常编码要删除，下同
        input输出的是字符串类型
        eval与float的区别在于eval会直接获取控制台输入的值，float则是将输入的字符串强制转换为浮点数
        此处用float与eval效果相似，优劣未知
        '''
        x1 = float(input("请输入第一个坐标x值："))
        y1 = float(input("请输入第一个坐标y值："))
        x2 = float(input("请输入第二个坐标x值："))
        y2 = float(input("请输入第二个坐标y值："))
        xy_list = [x1, y1, x2, y2]
        
        return xy_list

    def cal_distance(self, xy_list):
        '''
        计算两个坐标，返回两坐标距离
        xy_list:两个点的xy坐标的列表
        '''
        '''
        def cal_distance(self, xy_list):
        def 告诉python这是一个函数
        cal_distance 这是函数名称
        self，要写不写报错，表示 “这个类” 
        xy_list，def后面加这个，后面调用时要传值进来，不传报错
        '''
        length = math.sqrt((xy_list[0]-xy_list[2])**2 + (xy_list[1]-xy_list[3])**2)

        return length

    def go(self):
        '''
        开始运行类中函数逻辑
        '''
        '''
        此函数名字可改，负责传参，函数间的逻辑实现
        '''
        xy_list = self.in_xy()
        length = self.cal_distance(xy_list)
        print("两点距离为：", length)

class CalculateDistance2():
    '''
    CalculateDistance：计算距离,使用字典的方式存值
    '''
    def in_xy(self):
        '''
        输入两点的浮点数坐标，并返回两个坐标的列表
        '''
        xy_dir = {}
        for i in ['1', '2']:
            for j in ['x', 'y']:
                xy_value = float(input("请输入" + j + i + "："))
                xy_dir[j + i] = xy_value
        
        return xy_dir

    def cal_distance(self, xy_dir):
        '''
        计算两个坐标，返回两坐标距离
        '''
        length = math.sqrt((xy_dir['x1']-xy_dir['x2'])**2 + (xy_dir['y1']-xy_dir['y2'])**2)

        return length

    def go(self):
        '''
        调用类的时候只要调用此函数就能运行整个函数逻辑，此函数名字可改
        '''
        xy_dir = self.in_xy()
        length = self.cal_distance(xy_dir)
        print("两点距离为：", length)


if __name__ == "__main__":
    '''
    运行开始程序，出现错误输入时，中止运行并在控制台中打印输入错误
    '''
    '''
    if __name__ == "__main__":的意思是当在此py文件调用时运行，如果不是在此文件中运行，而是调用此文件中的函数时不运行以下编码
    方便后续函数跨文件调用，输入main选择第一个，会自动生产函数
    try后面接要运行的程序
    except后面接当程序出错时怎么做，是为了抛出异常
    ValueError是条件，此处是值错误时，可换别的值
    用法与if...else类似，注意要加try和except后加引号
    不懂百度关键词：python 异常
    注释其中CalculateDistance1().go()是为了让第一个别跑
    '''
    try:
        "运行计算距离1的go函数"
        CalculateDistance1().go()
        # CalculateDistance1().go() 
        CalculateDistance2().go()
    except ValueError:
        print("输入错误，请重新输入")
