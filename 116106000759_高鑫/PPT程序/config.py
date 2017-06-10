from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
def getconfig():
    d={'http://127.0.0.1:5556/wd/hub':DesiredCapabilities.CHROME,
       'http://127.0.0.1:5555/wd/hub':DesiredCapabilities.FIREFOX,
      }
    return d
