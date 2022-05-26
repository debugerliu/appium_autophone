from phone_page.base_page import BasePage


class MemberInvite(BasePage):

    def addmember_by_manul(self):
        from contact_add import ContactAdd
        self._driver.find_element_by_xpath('//*[@text="手动输入添加"]').click()
        return ContactAdd(self._driver)
