import pytest


# def re_data_list():
#     list_data = []
#     with open(r"D:\Python\Appium\four\data\data1.txt", 'r') as f:
#         for i in f.readlines():
#             list_data.append(eval(i.split('=')[-1]))
#         print(i)
#     return list_data 

class TestPara:

    @pytest.mark.parametrize('one, two', [(1, 2), (3, 4)])
    def test_p1(self, one, two):
        # print(three:%s, four:%s" % (one, two))
        print(one, two)
        assert one + two == 2, '结果不等于7'
