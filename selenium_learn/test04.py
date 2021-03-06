from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Firefox()
driver.get("https:192.168.82.186:8443")
user_textbox = driver.find_element_by_css_selector(".form-control.free_form_user")
user_textbox.send_keys("userS")
pwd_textbox = driver.find_element_by_css_selector(".form-control.free_form_pass")
pwd_textbox.send_keys("1234")
# 回车登录
pwd_textbox.send_keys(Keys.ENTER)
time.sleep(5)
# 智能等待
def wait_el(driver, func):
    return WebDriverWait(driver, 10).until(func)
side_button = wait_el(driver, lambda driver: driver.find_element_by_css_selector(".sidebar-toggle"))
side_button.click()
# 右键
ActionChains(driver).context_click(side_button).perform()
# 双击
ActionChains(driver).double_click(side_button).perform()
# 悬停
sidebar_menu = driver.find_elements_by_css_selector(".nav.sidebar-menu>li>a")
for el in sidebar_menu:
    ActionChains(driver).move_to_element(el).perform()
    time.sleep(3)
celue_guanli = driver.find_element_by_link_text("策略管理")
celue_guanli.click()
fatiao_shixing = driver.find_element_by_link_text("法条施行对照单")
ActionChains(driver).double_click(fatiao_shixing).perform()
alert_confirm = driver.find_element_by_css_selector(".confirm")
alert_confirm.click()
driver.quit()
