from appium import webdriver
from unittest import TestCase
from uiautomation_pkg_common_webdriver import *


class ProjectBase(TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
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
        # self.driver = webdriver.Remote(
        #     command_executor='http://127.0.0.1:4723/wd/hub',
        #     desired_capabilities={
        #         'platformName': 'iOS',
        #         'platformVersion': '11.2',
        #         'deviceName': 'iPad Pro (9.7-inch)',
        #         'browserName': 'Safari',
        #         'udid': '82DDA8DC-3D06-467B-8537-D3939672B050',
        #         'newCommandTimeout': 7200,
        #         'fullReset': True,
        #         'noReset': False,
        #         'automationName': 'XCUITest'
        #     })
        # self.driver = webdriver.Remote(
        #     command_executor='http://127.0.0.1:4723/wd/hub',
        #     desired_capabilities={
        #         'platformName': 'Android',
        #         'platformVersion': '6.0.1',
        #         'deviceName': 'Nexus 7',
        #         'browserName': 'Chrome',
        #         'chromedriverExecutable': '/Users/khaile/Develop/appiumTest/node_modules/appium-chromedriver/chromedriver/mac/chromedriver',
        #         'newCommandTimeout': 7200
        #     })
        self.driver.implicitly_wait(5)
        self.app = Device(self.driver)
        self.UIType = Type(self.driver)
        self.verification = Verify()
        self.assertion = Assert()
        self.app.switchToWebview()
        self.isMobile = self.app.isMobile()
        self.isIos = self.app.isIos()
        self.isChromium = False
        if self.driver.current_context == 'CHROMIUM':
            self.isChromium = True

    def tearDown(self):
        if self.assertion.didThrowError():
            try:
                self.app.saveScreenshot(self.id(), path=self.screenshotPath)
            except:
                pass
        self.driver.quit()