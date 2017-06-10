import time
from selenium import webdriver
from selenium.webdriver import Remote
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import config #导入 config.py 文件
#通过 host,browser 来参数化脚本
for host,browser in config.getconfig().items():
    print(host)
    print(browser)
    driver = webdriver.Remote(
    command_executor=host,
    desired_capabilities=browser
    )
    driver.get("http://www.baidu.com")
    driver.find_element_by_id("kw").send_keys("hello")
    driver.find_element_by_id("su").click()
    time.sleep(5)
    driver.close()