from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Firefox()
driver.get("https:192.168.82.186:8443")
user_textbox = driver.find_element_by_css_selector(".form-control.free_form_user")
user_textbox.send_keys("userS")
pwd_textbox = driver.find_element_by_css_selector(".form-control.free_form_pass")
pwd_textbox.send_keys("1234")
driver.find_element_by_css_selector(".btn").click()

time.sleep(5)
# 建立下拉框对象
driver.switch_to.frame("iframe_page_1")
select_box = Select(driver.find_element_by_css_selector(".form-control"))
select_box.select_by_index(0)
time.sleep(2)
select_box.select_by_index(1)
time.sleep(2)
select_box.select_by_index(2)
time.sleep(2)
select_box.select_by_value("-200")
time.sleep(2)
select_box.select_by_value("-130")
time.sleep(2)
select_box.select_by_value("-180")
time.sleep(2)
select_box.select_by_visible_text("异常管理")
time.sleep(5)
print(select_box.options)
print(select_box.first_selected_option)
print(select_box.all_selected_options)
driver.quit()
