from selenium import webdriver
import time
from selenium.webdriver import Remote
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import WebDriverException
driver=webdriver.Remote(
  
    desired_capabilities=DesiredCapabilities.HTMLUNIT
    )

driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("htmlunit")
driver.find_element_by_id("su").click()
time.sleep(2)
#driver.get_screenshot_as_file("E:\\run_htmlunit.jpg")
#driver.save_screenshot("E:\\run_htmlunit.jpg")
driver.quit()