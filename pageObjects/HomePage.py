from selenium.webdriver.common.by import By


class HomePage:
    shop = (By.LINK_TEXT, "Shop")  # this is the shop locator

    # defining constructor to bring the driver from the test present in test_e2e.py
    def __init__(self, driver):
        self.driver = driver  # the self.driver is the class variable and rhs driver is the one sent
        # during object creation

    def shop_items(self):
        return self.driver.find_element(*HomePage.shop)  # * unpacks the tuple
        # driver.find_element(By.LINK_TEXT, "Shop") -- This is same as the above step, just used tuple for the locator
        # which is a class variable
        # returning it so that we can catch this in the test file

