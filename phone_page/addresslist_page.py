from phone_page.base_page import BasePage
from phone_page.member_invit import MemberInvite


class AddressList(BasePage):

    def add_member(self):
        self._driver.find_element_by_xpath("//*[@resource-id='com.tencent.wework:id/kor']").click()
        self._driver.find_element_by_xpath('//*[@text="添加成员"]').click()
        return MemberInvite(self._driver)
