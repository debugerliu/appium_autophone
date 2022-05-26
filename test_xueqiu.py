from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestDW:
    def setup(self):
        desired_caps = {'platformName': 'Android',
                        'platformVersion': '7.1',
                        'deviceName': '127.0.0.1:62001',
                        'appPackage': 'com.xueqiu.android',
                        'appActivity': 'com.xueqiu.android.main.view.MainActivity',
                        'automationName': 'uiautomator2',
                        'noReset': True}
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize('search, type', [('阿里巴巴', 'BABA'), ('xiaomi', '01810')])
    def test_search(self, search, type):
        print('搜索测试用例')
        self.driver.find_element_by_xpath(
            '//*[@resource-id="com.xueqiu.android:id/tv_banner"]/android.widget.ViewFlipper').click()
        self.driver.find_element_by_xpath(
            '//*[@resource-id="com.xueqiu.android:id/search_input_text"]').send_keys(search)
        self.driver.find_element_by_xpath(
            f'//*[@text="{type}"]').click()
        price = self.driver.find_element_by_xpath(
            f"//*[@text='{type}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        print(price)
        sleep(5)

    def test_touch(self):
        action = TouchAction(self.driver)
        print(self.driver.get_window_rect())
        action.press(x=200, y=1000).wait(500).move_to(x=360, y=0).release().perform()
        sleep(5)
