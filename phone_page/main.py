from phone_page.base_page import BasePage


class Main(BasePage):

    def goto_message(self):
        pass

    def goto_add_list(self):
        from phone_page.addresslist_page import AddressList
        self._driver.find_element_by_xpath('//*[@text="通讯录"]').click()
        return AddressList(self._driver)

    def goto_work(self):
        pass

    def goto_profile(self):
        pass
