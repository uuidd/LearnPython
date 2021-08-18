# 导入webdrvier
from selenium import webdriver
import time

# 指定chromedriver路径
driver = webdriver.Chrome('C:\Program Files\Google\Chrome\Application\chromedriver.exe')
# 访问小黑屋
url = 'http://adarkroom.doublespeakgames.com/?lang=zh_cn'
driver.get(url)
time.sleep(10)

# def __init__(self):
#         self.driver = webdriver.Chrome('C:\Program Files\Google\Chrome\Application\chromedriver.exe')
#         url = 'http://adarkroom.doublespeakgames.com/?lang=zh_cn'
#         self.driver.get(url)

# #游戏设置
# a = driver.switch_to_alert()
# # 打印弹出框文本内容
# print(a.text)
# Sound = driver.find_element_by_link_text('enable audio')    #选择声音
# # language = driver.find_element_by_xpath('/html/body/div[2]/span[5]')    #语言为简体中文
# # language.click()
# speed = driver.find_element_by_xpath('/html/body/div[2]/span[5]')   #设置速度为加速
# speed.click()
# yes_speed = driver.find_element_by_id('yes')  #确认加速
# yes_speed.click()


# 定位到生火按钮
fire = driver.find_element_by_id('lightButton')
logging = driver.find_element_by_id('gatherButton')
trap = driver.find_element_by_id('trapsButton')
# 意外
event = driver.find_element_by_id("event")
sound = driver.find_element_by_xpath('//*[@id="yes"]').get_attribute('textContent')
# investigate = driver.find_element_by_id("ignore")
# qigai = driver.find_element_by_id("deny")
# build= driver.find_element_by_id("deny")        #两部（修）
# zaosheng = driver.find_element_by_id("ignore")
# liulang = driver.find_element_by_id("deny")
# end == driver.find_element_by_id("end")       #可归类

# 设置输入控制循环次数
# loop = int(input("请输入循环次数"))

for i in range(120):
    # loop = loop -1
    if event == "event":
        if sound == "enable audio":
            sound.click()

    else:
        fire.click()
        logging.click()
        trap.click()
        time.sleep(10)

time.sleep(3)
