from selenium import webdriver
import time

driver = webdriver.Firefox()

# 请求url响应
url1 = "http://www.baidu.com/"
driver.get(url1)

url2 = "http://www.ilxdh.com/" 
driver.get(url2)
# 窗口最大化
driver.maximize_window()
# 后退，疑似Firefox的bug需要两次回退才能正常后退
driver.back()
driver.back()
# 前进
driver.forward()
# 窗口位置
driver.set_window_position(100, 100)

# 窗口大小
driver.set_window_size(600, 600)
# driver.quit()

# 显示当前的url
driver.current_url
# 显示当前的页面标题
driver.title
# 获取网站源码
driver.page_source 
# 直接保存文件保存快照操作
driver.get_screenshot_as_file("C:/Users/Zz/Desktop/1.jpg")
# 保存快照操作2，二进制文件
png1 = driver.get_screenshot_as_png()
# 写入二进制文件，用“wb”
with open("C:/Users/Zz/Desktop/2.jpg", "wb") as f:
    f.write(png1)
# 退出浏览器
driver.close()