from appium import webdriver
from unittest import TestCase
from uiautomation_pkg_common_webdriver import *
import os


class ProjectBase(TestCase):
    def setUp(self):
        user = 'mmqaautomation@gmail.com'
        key = '13iWH3WClJ1auYT0fBR6-ZYsUAI0O24DyD6uBKOPW'
        version = 'placeholderVersion'
        runId = 'placeholderRunId'
        self.caseId = ''
        self.client = APIClient(runId=runId, version=version, user=user, key=key)
        """Below is the template to set up your test run"""
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
        # """ Below is an example of a set up for iOS device """
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
        # """ Below is an example of a set up for Android device"""
        # os.system('adb shell input keyevent KEYCODE_WAKEUP') #To keep Android device awake
        # self.driver = webdriver.Remote(
        #     command_executor='http://127.0.0.1:4723/wd/hub',
        #     desired_capabilities={
        #         'platformName': 'Android',
        #         'platformVersion': '7.0',
        #         'deviceName': 'Galaxy',
        #         'browserName': 'Chrome',
        #         'newCommandTimeout': 7200
        #     })
        #
        # self.driver.implicitly_wait(5)
        # self.app = Device(self.driver)
        # self.UIType = Type(self.driver)
        # self.verification = Verify()
        # self.assertion = Assert()
        # self.app.switchToWebview()
        # self.isMobile = self.app.isMobile()
        # self.isIos = self.app.isIos()
        # self.isChromium = self.app.isChromium()
        # self.isSafari = self.app.isSafari()
        # self.screenshotPath = '../../screenshots/'
        # self.app.createScreenshotDir(self.screenshotPath)

    def tearDown(self):
        if self.assertion.didThrowError():
            resultFlag = False
            try:
                self.app.saveScreenshot(self.id(), path=self.screenshotPath)
            except:
                pass
        else:
            resultFlag = True
        try:
            self.client.updateTestrail(self.caseId, resultFlag)
        except:
            pass
        finally:
            self.driver.quit()