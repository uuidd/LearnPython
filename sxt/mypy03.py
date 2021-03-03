def learn_list(self):
    b = list(range(10))
    b = list(i*2 for i in range(10))
    b = list(i*2 for i in range(1,100) if i%2 == 0)
    b = list(range(10,100,10))
    b = b[:]
    b = b[4::2]
    b = b[1:]
    b = b[:2]
    b.sort(reverse=True)
    print(b[::-1])

def score_degree(self):
    score = int(input("请输入一个分数："))
    degree = "ABCDE"
    if score > 100 | score < 0:
        print("请输入一个0-100的分数")
    else:
        num = score//10
        if num < 6:
            num = 5
    print("分数是{0}，等级为{1}".format(score, degree[9-num]))

def print_table(self):
    names = ("张三", "李四", "王五")
    ages = (18, 32, 23)
    jobs = ("qa", "dev", "ops")

    for name, age, job in zip(names, ages, jobs):
        print("{0}--{1}--{2}".format(name, age, job))

def yel_test(self):
    cells = [(row, col) for row in range(1, 10) for col in range(1,10)]
    print(cells)

    list_a = [a for a in "asdfghjkl"]
    print(list_a)

    my_text = "i love liqiongyu, i love you very much"
    char_count = {c:my_text.count(c) for c in my_text}
    print(char_count)

    char_b = {x for x in range(1, 100) if x%9==0}
    print(char_b)

    # 迭代器只能用一次
    gnt = (x for x in range(4))
    print(tuple(gnt))
    print(tuple(gnt))


# *param（一个星号），将多个参数收集到一个元组对象中
# **param（两个星号），将多个参数收集到个“字典”对象中
def param_test1(a, b, *c):
    print(a, b, c)
    
    # param_test1(1, 2, 3, 4, 5)
    # 1 2 (3, 4, 5)

def param_test2(a, b, **c):
    print(a, b, c)

    # param_test2(1, 2, name='qiongyu', age=22)
    # 1 2 {'name': 'qiongyu', 'ago': 22}

def param_test3(a, b, *c, **d):
    print(a, b, c, d)

    # param_test3(1, 2, 3, 4, 5, name='qiongyu', age=22)
    # 1 2 (3, 4, 5) {'name': 'qiongyu', 'age': 22}

def outer_test():
    b = 10

    def inner():
        nonlocal b
        print("inner b：", b)
        b = 20

        global inner_a
        inner_a = 1000

    inner()
    print("outer b：", b)

# outer_test()
# print("inner_a:", inner_a)

# inner b： 10
# outer b： 20
# inner_a: 1000

 
