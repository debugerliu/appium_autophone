import time

from appium import webdriver

desired_caps = {'platformName': 'Android',
                'platformVersion': '7.1',
                'deviceName': '127.0.0.1:62001',
                'appPackage': 'com.tencent.android.qqdownloader',
                'appActivity': 'com.tencent.assistantv2.activity.MainActivity',
                'automationName': 'uiautomator2',
                'noReset': True}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)


el1 = driver.find_element_by_id('com.tencent.android.qqdownloader:id/awt')
el1.click()

el2 = driver.find_element_by_accessibility_id(r'在这里输入搜索内容')
el2.send_keys("淘宝")
time.sleep(3)
driver.quit()



