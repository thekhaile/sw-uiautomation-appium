from appium import webdriver
from common import *


def main():
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723/wd/hub',
        desired_capabilities={
            'platformName': 'iOS',
            'platformVersion': '11.0',
            'deviceName': 'iPad Pro (9.7-inch)',
            'browserName': 'Safari',
            'udid': 'CEF5614C-6A13-4FF0-97A7-8F05BBB6BF0C',
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