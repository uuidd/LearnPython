# 导入re
import re
import json
from enum import Enum

class DataGrep():
    S1 = 'abc,acc,adc,aec,afc,ahc\n'
    A1 = "C|C++|Java|C#23|Pytho454n|JavaScr54ipt"
    S2 = 'life is short, i use python'
    def d1(self):
        print(self.A1.index('Python') > -1)

    def d2(self):
        # 字符集
        r = re.findall('a[cf]c', self.S1)    #取中间为c或f，两边为a、c的三位数的值
        r = re.findall('a[^cf]c', self.S1)    #取中间不为c或f，两边为a、c的三位数的
        r = re.findall('.', self.S1, re.S)    #取中间不为c到f，两边为a、c的三位数
        print(r)

    def d3(self):
        def convert(self):
            matched = self.group()
            return matched + 'hh'
        r =re.sub('bc',convert,self.S1)
        print(r)

    def d4(self):
        r = re.search('life(.*)python', self.S2)    #取life和python中间的值
        print(r.group(0,1,))    #group值要设置为1

        r = re.findall('life(.*)python', self.S2)     # 第二种方法
        print(r)
        print(r.groups())

    def d5(self):
        json_str = '[{"name":"qiyue", "age":18}, {"name":"qiyue", "age":18}]'    
        #转化JSON（array）数组要加中括号
        student = json.loads(json_str)
        print(type(student))
        print(student)
        # <class 'list'>
        # [{'name': 'qiyue', 'age': 18}, {'name': 'qiyue', 'age': 18}]

    def d6(self):
        student = [
            {"name":"qiyue", "age":18, "falg": False},
            {"name":"qiyue", "age":18}    #利用花括号换行，不需要加\反斜杠
          ]
        json_str = json.dumps(student)
        print(type(json_str))
        print(json_str)
        # <class 'str'>
        # [{"name": "qiyue", "age": 18, "falg": false}, {"name": "qiyue", "age": 18}]


class Vip(Enum):
    YELLOW = 1
    GREEN = 1
    BLACK = 3
    RED = 4
    
    def d7(self):
        print(type(Vip.GREEN.name))
        print(type(Vip.GREEN))
        # <class 'str'>
        # <enum 'Vip'>
        for v in Vip:
            print(v)
        # Vip.YELLOW
        # Vip.GREEN
        # Vip.BLACK
        # Vip.RED
        result = Vip.GREEN is Vip.GREEN
        print(result)
        # False
        
    def d8(self):
        for v in Vip.__members__:
            print(v)
        # ('YELLOW', <Vip.YELLOW: 1>)
        # ('GREEN', <Vip.YELLOW: 1>)
        # ('BLACK', <Vip.BLACK: 3>)
        # ('RED', <Vip.RED: 4>)
        a = 1
        print(Vip(a))