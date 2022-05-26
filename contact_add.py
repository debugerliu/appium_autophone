from phone_page.base_page import BasePage


class ContactAdd(BasePage):

    def input_name(self):

        self._driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/bu8']").send_keys('学习')
        return self

    # def set_gender(self):
    #     return self

    def input_phone_number(self):
        self._driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/hqa']").send_keys(12345679810)
        return self

    def click_save(self):
        self._driver.find_element_by_xpath('//*[@text="保存"]').click()
        from phone_page.member_invit import MemberInvite
        return MemberInvite(self._driver)
