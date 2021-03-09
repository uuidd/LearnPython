from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")
driver.find_element_by_id("kw").send_keys("李琼瑜")
driver.find_element_by_id("su").click()
driver.back()
driver.back()
driver.find_element(By.ID, "kw").send_keys("李毅辉")
driver.find_element(By.ID, "su").click()
time.sleep(20)
driver.close()
