import time

from selenium import webdriver

# 下拉操作selenium无法实现，只能依靠JavaScript
driver = webdriver.Firefox()
driver.get("http://ilxdh.com/")
driver.find_element_by_css_selector(".close-btn").click()
# 直接下拉到1000，下拉操作
# js1 = "var q = document.documentElement.scrollTop=1000"
# driver.execute_script(js1)
# js = "window.scrollTo(0,1000)"
# driver.execute_script(js)

# 持续下拉
for i in range(30):
    js2 = "window.scrollTo(0, %s)" % (i * 100)
    driver.execute_script(js2)
    time.sleep(0.1)
