from selenium import webdriver
import os


driver = webdriver.Firefox()

# 进入本目录的
file_path = 'file:///' + os.path.abspath("selenium_learn\\example_frame.html")

driver.get(file_path)

# 进入框架1/表单1
driver.switch_to.frame("itcast_frame1")
# 进入框架2/表单2，进入框架内才能定位到该框架的元素
driver.switch_to.frame("itcast_frame2")
el1 = driver.find_element_by_id("sb_form_q")
el1.send_keys("selenium")
el2 = driver.find_element_by_id("sb_form_go")
el2.click()

driver.switch_to.default_content()
# 退回最出表单
try:
    driver.find_element_by_id("sb_form_go")
except:
    print('已从表单中退出')