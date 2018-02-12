from appium import webdriver
from unittest import TestCase
from common import *


class ProjectBase(TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
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
        self.driver.implicitly_wait(5)
        self.app = Device(self.driver)
        self.UIType = Type(self.driver)
        self.verification = Verify()
        self.assertion = Assert()
        self.isMobile = self.app.isMobile()

    def tearDown(self):
        self.driver.quit()