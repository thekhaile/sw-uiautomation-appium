from appium import webdriver
from common import *


def main():
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723/wd/hub',
        desired_capabilities={
            'platformName': 'platformNamePlaceholder',
            'platformVersion': 'platformVersionPlaceholder',
            'deviceName': 'deviceNamePlaceholder',
            'browserName' 'browserNamePlaceholder'
            'udid': 'udidPlaceholder',
            'newCommandTimeout': 7200,
            'fullReset': True,
            'noReset': False,
            'automationName': 'XCUITest'
        })
    global app
    global UIType
    app = Device(driver)
    UIType = Type(driver)

main()