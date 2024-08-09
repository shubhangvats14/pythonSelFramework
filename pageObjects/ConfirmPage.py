from selenium.webdriver.common.by import By


class ConfirmPage:
    country_name = (By.LINK_TEXT, "India")
    purchase_btn = (By.XPATH, "//input[@class='btn btn-success btn-lg']")
    success_msg = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def __init__(self, driver):
        self.driver = driver

    def get_country_name(self):
        return self.driver.find_element(*ConfirmPage.country_name)

    def get_purchase_btn(self):
        return self.driver.find_element(*ConfirmPage.purchase_btn)

    def get_success_msg(self):
        return self.driver.find_element(*ConfirmPage.success_msg)
