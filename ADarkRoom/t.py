# from selenium import webdriver

# driver = webdriver.ActionChains()
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome(r'C:\Program Files\Google\Chrome\Application\chromedriver.exe')  # 指定chromedriver路径
# driver.get('http://adarkroom.doublespeakgames.com/?lang=zh_cn')
# brower.quit()

driver.get("https://www.baidu.com")
driver.maximize_window()
# 点击百度登录按钮
driver.find_element_by_xpath('//*[@id="u1"]//a[@name="tj_login"]').click()

# 等待百度登录弹出框中 要出现的元素可见
ele_id = "TANGRAM__PSP_10__footerULoginBtn"
param = (By.ID, ele_id)
# 元素可见时，再进行后续操作
WebDriverWait(driver, 10).until(ec.visibility_of_element_located(param))

driver.find_element_by_id(ele_id).click()
time.sleep(5)
driver.quit()
