class Beginner():
    def c1(self):
        # print("hello world")
        mood = False
        if mood :
            print("go left")
        else :
            print("go right")

    def c2(self):
        account = 'qiyue'
        password = '123456'
        print('please input account')
        user_account = input()
        print('plesase input password')
        user_password = input()

        if account == user_account and password == user_password :
            print('success')
        else :
            print('fail')

    def c3(self):
        a = [['apple','orange','banana','grape'],(1,2,3)]
        for x in a:
            for y in x:
                if y == 3:
                    continue
                print(y)
        else:
            print('pass')

    def c4(self):
        a = [1,2,3,4,5,6,7,8]
        for i in range(0, len(a), 2):
            print(a[i], end=" | ")
        b = a[0:len(a):2]
        print(b)

    def c5(self):
        '''
        This is a c9 doc                          #注释
        '''
        print('name:' + __name__)                    # + 把他们连接在一起，

        print('doc:' + __doc__)                      #doc指的是模块的注释
        print('file:' + __file__)

    def c6(self):
        print('~~~~~~~~~~c6~~~~~~~~~~')
        print('package:' + (__package__ or '当前模块不属于任何包'))
        print('name:' + __name__)
        print('doc:' + (__doc__ or '当前模块没有文档注释'))
        print('file:' + __file__)

    def c7(self):
        if __name__ == '__main__':
            print('This is app')
        else:
            print('This is a module')

class Student1():
    name = ''
    age = 0
    # 类变量
    def __init__(self, name, age):
        # 构造函数
        self.age = age
        self.name = name
        # 实例变量，用于保存存入函数的值

class Person():
    sum = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_name(self):
        print(self.name)

class Student2(Person):
    def __init__(self, school, name, age):
        self.school = school
        super(Student2, self).__init__(name, age)
        Person.__init__(self, name, age)    #实现在子类的构造函数中调用父类的构造函数
    
    def do_homework(self):
        print('english homework')
