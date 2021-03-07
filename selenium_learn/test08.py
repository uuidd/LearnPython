from selenium import webdriver



driver = webdriver.Firefox()
driver.get("https://192.168.82.186:8443")
user_textbox = driver.find_element_by_css_selector(".form-control.free_form_user")
user_textbox.send_keys("userS")
pwd_textbox = driver.find_element_by_css_selector(".form-control.free_form_pass")
pwd_textbox.send_keys("1234")
driver.find_element_by_css_selector(".btn").click()
# 获取所有cookie
cookies = driver.get_cookies()
print(cookies)
# 删除所有cookie
driver.delete_all_cookies()
# 添加cookie
driver.add_cookie(cookies[0])
cookies1 = driver.get_cookies()
print(cookies1)
driver.quit()