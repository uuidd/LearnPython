from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# 预期条件类，名字太长，起EC别名
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()
driver.get("https://192.168.82.186:8443")
user_textbox = driver.find_element_by_css_selector(".form-control.free_form_user")
user_textbox.send_keys("userS")
pwd_textbox = driver.find_element_by_css_selector(".form-control.free_form_pass")
pwd_textbox.send_keys("1234")
driver.find_element_by_css_selector(".btn").click()
# 等待表单加载完毕，显示等待
frame1 = WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.ID, "iframe_page_1")))
driver.switch_to.frame(frame1)
refresh_btn = WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn_refresh")))
refresh_btn.click()
time.sleep(1)
refresh_btn.click()
time.sleep(1)
refresh_btn.click()
time.sleep(1)
driver.switch_to.default_content()
# 隐式等待，最多等待几秒等元素出现，全局，常用，无需导入
driver.implicitly_wait(10)
driver.quit()
