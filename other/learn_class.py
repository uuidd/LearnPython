class LearnClass():
    def curve_pre(self):
        a = 25    #环境变量
        def curve(x):    #函数
            return a * x * x
        return curve

    def go_curve(self):
        f = self.curve_pre()
        print(f(2))
        print(self.curve_pre()(2))

    # def f1(self):
    #     a = 10
    #     def f2(self):
    #         a = 20    #局部变量
    #         print(a)
    #     print(a)    #f2未被执行
    #     self.f1().f2()
    #     print(a)
    
    # def go_f1(self):
    #     LearnClass().f1()

    origin = 0
    def factory(self, pos):
        def go(step):
            nonlocal pos
            new_pos = pos + step
            pos = new_pos
            return new_pos
        return go

    def go_factory(self):
        f = self.factory(self.origin)
        print(f(2))
        print(f(2))
        print(f(2))