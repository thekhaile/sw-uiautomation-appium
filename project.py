from appium import webdriver
from uiautomation_pkg_common_webdriver import *


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
    # driver = webdriver.Remote(
    #     command_executor='http://127.0.0.1:4723/wd/hub',
    #     desired_capabilities={
    #         'platformName': 'iOS',
    #         'platformVersion': '11.0',
    #         'deviceName': 'iPad Pro (9.7-inch)',
    #         'browserName': 'Safari',
    #         'udid': '82DDA8DC-3D06-467B-8537-D3939672B050',
    #         'newCommandTimeout': 7200,
    #         'fullReset': True,
    #         'noReset': False,
    #         'automationName': 'XCUITest'
    #     })
    # driver = webdriver.Remote(
    #     command_executor='http://127.0.0.1:4723/wd/hub',
    #     desired_capabilities={
    #         'platformName': 'Android',
    #         'platformVersion': '6.0.1',
    #         'deviceName': 'Nexus 7',
    #         'browserName': 'Chrome',
    #         'chromedriverExecutable': '/Users/khaile/Develop/appiumTest/node_modules/appium-chromedriver/chromedriver/mac/chromedriver',
    #         'newCommandTimeout': 7200
    #     })
    global app
    global UIType
    app = Device(driver)
    UIType = Type(driver)

main()