#!/usr/bin/env python
# -*- encoding: utf-8 -*-



class StudentSort():
    '''
    第4题，根据学生成绩排序，并输出
    '''
    def student_sort(self):
        '''
        降序排序学生成绩
        '''
        '''
        特别注释，正常没有同时这样两个注释的，正常只会有一个注释，给别人看时请删除，下同
        字典，不用换行符，我记错了
        '''
        student_info = [{'学号' : 1001, '姓名' : 'Tom', '成绩' : 98},
        {'学号' : 1002, '姓名' : 'Jerry', '成绩' : 95},
        {'学号' : 1003, '姓名' : 'Mary', '成绩' : 73}, 
        {'学号' : 1004, '姓名' : 'May', '成绩' : 87},
        {'学号' : 1005, '姓名' : 'Jack', '成绩' : 46}]

        return sorted(student_info, key=lambda x:x['成绩'], reverse=True)   #这行看不懂，链接：https://blog.csdn.net/ustbbsy/article/details/79637594  lambda叫做匿名函数，python特有的会经常看到，B站老师的课有讲，不懂度娘，多打几遍就理解了
    
    def print_info(self, stu_sorted):
        '''
        打印最后结果，以“学号：XXXX 名字：XXX 成绩：XX”的格式输出
        stu_sorted ： 输入排序好的学生列表
        '''
        for i in stu_sorted:
            for j in i:
                print(j + '：' + str(i[j]) + ' ' , end='')  #遍历列表，以固定格式输出
            print(end='\n') #遍历字典，结果打印换行符

    def pt_result(self, stu_sorted):
        '''
        打印最后结果，以类似表格形式输出
        stu_sorted ： 输入排序好的学生列表
        '''
        '''
        第二种输出方式，学会封装函数，输入输出什么可以灵活改变，相当好用
        '''
        print("学号 姓名 成绩")
        for i in stu_sorted:
            for j in i:
                print(i[j], end=' ') 
            print(end='\n')

    def go(self):
        '''
        开始运行
        '''
        stu_sorted = self.student_sort()
        self.print_info(stu_sorted)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        self.pt_result(stu_sorted)

if __name__ == "__main__":
    '''
    程序所有异常全部抛出，并在控制台显示 “出错”
    '''
    '''
    不在本文件运行，则不运行以下代码
    '''
    try:
        # StudentSort().pt_result()
        StudentSort().go()
    except BaseException:
        print('出错')

