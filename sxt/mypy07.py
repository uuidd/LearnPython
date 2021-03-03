
try:
    pass
except:
    pass
else:
    pass
finally:
    pass

class GenderException(Exception):
    def __init__(self):
        super().__init__()
        self.errMsg = '性别只能设置成男或女'

class Student:
    def __init__(self, name, gender):
        self.name = name
        self.set_gender(gender)
    
    def set_gender(self, gender):
        if gender == '男' or gender == '女':
            self.__gender = gender
        else:
            raise GenderException()

    def get_gender(self):
        return self.__gender

    def show_info(self):
        print("我叫：%s 性别：%s"%(self.name, self.__gender))

    # 合并接口
    gender = property(get_gender, set_gender)


stu1 = Student("李四", '女') 

print(stu1.gender)
stu1.gender = '男'
print(stu1.gender)

try:
    stu1.set_gender('ss')
except Exception as e:
    # print(type(e))
    print(e.errMsg)
