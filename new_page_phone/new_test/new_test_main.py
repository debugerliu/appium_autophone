from time import sleep

import pytest
import yaml

from new_page_phone.new_page.new_app import App


class TestNewMain:
    @pytest.mark.parametrize('value1, value2', yaml.safe_load(open(r'test_main.yaml')))
    def test_main(self, value1, value2):
        # self.app = App()
        # self.main = self.app.start().main().goto_search_page()
        # sleep(1)
        print(value1)
        print(value2)


