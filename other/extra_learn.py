from urllib import request

class Spider():
    url = 'https://www.huya.com/g/hearthstone'
    
    # 抓取内容
    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        str(htmls, encoding='utf-8')
        print(htmls)
        return htmls

    def go(self):
        self.__fetch_content()

class Switch():
    day = 7

    switcher = {
        0 : get_Sunday,
        1 : get_Monday,
        2 : get_Tuesday
    }

    def get_Sunday(self):
        return 'Sunday'
    def get_Monday(self):
        return 'Monday'
    def get_Tuesday(self):
        return 'Tuesday'
    def get_default(self):
        return 'Unkown'
    
    def go_switch(self):
        day_name = self.switcher.get(self.day, self.get_default)()
        print(day_name)

class ExtraLearn():
    def r1(self):
        a = {1,2,3,4,5,5,6}
        b = {i **2 for i in a if i>=5}
        print(b)

    def r2(self):
        students ={
            '喜小乐':18,
            '石敢当':20,
            '横小五':15
        }
        b = {value:key for key, value in students.items()}
        print(b)

class BoolTest():
    def __bool__(self):
        return False
    def __len__(self):
        return 0
    def go_test_bool(self):
        print(bool(BoolTest()))