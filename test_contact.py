from phone_page.app import App


class TestContcat:
    def setup(self):
        self.app = App()
        self.main = self.app.start().main()

    def test_addcontact(self):
        self.main.goto_add_list().add_member().addmember_by_manul().input_name().input_phone_number().click_save()
