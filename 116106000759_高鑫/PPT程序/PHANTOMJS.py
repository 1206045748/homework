from selenium import webdriver
import time
from selenium.webdriver import Remote
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import WebDriverException
driver=webdriver.PhantomJS(executable_path="C:\Python\Scripts\phantomjs.exe")
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("hello")
driver.find_element_by_id("su").click()
time.sleep(2)
driver.get_screenshot_as_file("E:\\run_phantomjs.jpg")
driver.close()