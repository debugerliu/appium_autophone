from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestDW:
    def setup(self):
        desired_caps = {'platformName': 'Android',
                        'platformVersion': '7.1',
                        'deviceName': '127.0.0.1:62001',
                        'appPackage': 'com.android.settings',
                        'appActivity': 'com.android.settings.Settings',
                        'automationName': 'uiautomator2',
                        'noReset': True}
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        print('搜索测试用例')
        self.driver.find_element_by_id('com.tencent.android.qqdownloader:id/awt').click()
        self.driver.find_element_by_accessibility_id(r'在这里输入搜索内容').send_keys('淘宝')
        self.driver.find_element_by_xpath('//*[@class="android.widget.TextView" and @text="淘宝"]').click()
        tt = self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView[1]').text
        print(tt)
        sleep(5)

    def test_touch(self):
        action = TouchAction(self.driver)
        print(self.driver.get_window_rect())
        action.press(x=200, y=1000).wait(500).move_to(x=360, y=0).release().perform()
        sleep(5)
