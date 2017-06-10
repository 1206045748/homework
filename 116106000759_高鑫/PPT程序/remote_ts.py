import time
from selenium import webdriver
from selenium.webdriver import Remote
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
driver=webdriver.Remote(
    command_executor='http://127.0.0.1：4444/wd/hub',
    desired_capabilities=DesiredCapabilities.CHROME
	)
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("hello")
driver.find_element_by_id("su").click()
time.sleep(5)
driver.close()