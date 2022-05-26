from new_page_phone.new_page.new_main import Main
from phone_page.base_page import BasePage

from appium import webdriver


class App(BasePage):
    def start(self):
        if self._driver == None:
            desired_caps = {'platformName': 'Android',
                            'platformVersion': '7.1',
                            'deviceName': '127.0.0.1:62001',
                            'appPackage': 'com.xueqiu.android',
                            'appActivity': 'com.xueqiu.android.main.view.MainActivity',
                            'automationName': 'uiautomator2',
                            # 'dontStopAppOnReset': True,
                            'noReset': True}
            self._driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        else:
            self._driver.launch_app()

        self._driver.implicitly_wait(3)
        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self) -> Main:
        return Main(self._driver)
