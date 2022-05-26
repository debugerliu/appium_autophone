from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.extensions.android.gsm import GsmCallActions


class TestBrowser:
    def setup(self):
        desired_caps = {'platformName': 'Android',
                        'platformVersion': '7.1',
                        'deviceName': '127.0.0.1:62001',
                        'browserName': 'Browser',
                        'automationName': 'uiautomator2',
                        'noReset': True}
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get('http://m.baidu.com')
        self.driver.find_element_by_xpath('//*[@for="index-kw"]').click()
        sleep(2)
        print('执行了1')
        self.driver.find_element_by_xpath('//*[@id="index-kw"]').send_keys('appium')
        sleep(2)
        print('执行了2')
        self.driver.find_element_by_xpath('//*[@id="index-bn"]').click()
        sleep(3)

    def test_phone_ese(self):
        self.driver.make_gsm_call('123123', GsmCallActions.CALL)
        self.driver.send_sms('123132', 'hello nima')

    def test_phone_photo(self):
        self.driver.get_screenshot_as_file('.img.png')