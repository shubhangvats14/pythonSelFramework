import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from TestData.HomePageData import HomePageData


@pytest.mark.usefixtures("form_data")
class TestHomePage(BaseClass):
    def test_form_submission(self, form_data):
        homepage_obj = HomePage(self.driver)

        homepage_obj.get_name().send_keys(form_data["name"])
        homepage_obj.get_email().send_keys(form_data["email"])
        homepage_obj.get_password().send_keys(form_data["password"])

        # generalized the drop-down select code, now defined in BaseClass
        self.select_dd_value(homepage_obj.get_gender(), "Male")

        homepage_obj.get_submit_btn().click()
        msg = homepage_obj.get_msg().text
        assert "Success" in msg
        self.driver.refresh()

    # defining fixture in the same file as this will be used by this case only
    # @pytest.fixture(params=[("Chrome", "Shubhang@fhg.com", "Vats"), ("Firefox", "Rahul@ghg.com", "Shetty"),
    #                         ("IE", "Vijay@ghvh.com", "Rana")]) -- using Tuples (disadvantage - key:value not present)
    @pytest.fixture(params=HomePageData.home_page_data)
    def form_data(self, request):
        return request.param
