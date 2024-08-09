from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:
    shop = (By.LINK_TEXT, "Shop")  # this is the shop locator
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit_btn = (By.XPATH, "//input[@value='Submit']")
    msg = (By.CSS_SELECTOR, "[class*='alert-success']")

    # defining constructor to bring the driver from the test present in test_e2e.py
    def __init__(self, driver):
        self.driver = driver  # the self.driver is the class variable and rhs driver is the one sent
        # during object creation

    def shop_items(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = CheckoutPage(self.driver)
        return checkoutpage
        # * unpacks the tuple
        # driver.find_element(By.LINK_TEXT, "Shop") -- This is same as the above step, just used tuple for the locator
        # which is a class variable
        # returning it so that we can catch this in the test file

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_email(self):
        return self.driver.find_element(*HomePage.email)

    def get_password(self):
        return self.driver.find_element(*HomePage.password)

    def get_gender(self):
        return self.driver.find_element(*HomePage.gender)

    def get_submit_btn(self):
        return self.driver.find_element(*HomePage.submit_btn)

    def get_msg(self):
        return self.driver.find_element(*HomePage.msg)
