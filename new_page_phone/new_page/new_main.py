from selenium.webdriver.common.by import By

from new_page_phone.new_page.base import BasePage


class Main(BasePage):

    def goto_search_page(self):
        # self.find(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/tv_banner"]/android.widget.ViewFlipper').click()
        self.steps(r'C:\Users\lxw\PycharmProjects\appium_autophone\new_page_phone\new_page\newmain.yaml')


