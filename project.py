from appium import webdriver
from uiautomation_pkg_common_webdriver import *
from southwire_pkg_uiautomation_webdriver.components import *

class Flow():
    def launch(self):
        # self.driver = webdriver.Remote(
        #     command_executor='http://127.0.0.1:4723/wd/hub',
        #     desired_capabilities={
        #         'platformName': 'platformNamePlaceholder',
        #         'platformVersion': 'platformVersionPlaceholder',
        #         'deviceName': 'deviceNamePlaceholder',
        #         'browserName' 'browserNamePlaceholder'
        #         'udid': 'udidPlaceholder',
        #         'newCommandTimeout': 7200,
        #         'fullReset': True,
        #         'noReset': False,
        #         'automationName': 'XCUITest'
        #     })
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'platformName': 'iOS',
                'platformVersion': '11.2',
                'deviceName': 'iPad Pro (9.7-inch)',
                'browserName': 'Safari',
                'udid': '82DDA8DC-3D06-467B-8537-D3939672B050',
                'newCommandTimeout': 7200,
                'fullReset': True,
                'noReset': False,
                'automationName': 'XCUITest'
            })
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
        self.isChromium = self.app.isChromium()
        self.isSafari = self.app.isSafari()

        # Initializing the objects specific to the project
        self.authentication = Authentication(self)
        self.circuits = Circuits(self)
        self.feederSchedule = FeederSchedule(self)
        self.jobs = Jobs(self)
        self.navigation = Navigation(self)
        self.projects = Projects(self)
        self.reels = Reels(self)
        self.registration = Registration(self)

    def quit(self):
        self.driver.quit()

def main():
    global flow
    flow = Flow()
    flow.launch()

main()