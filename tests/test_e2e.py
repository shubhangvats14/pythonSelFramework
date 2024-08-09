from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):  # using inheritance, we are inheriting the fixture properties of the BaseClass for
    # more code readability, now we need not define the fixture redundant code
    def test_e2e(self):  # here self is already loaded with the driver variable which was defined in the setup fixture,
        # so we don't need to add the setup parameter in this method
        homepage = HomePage(self.driver)  # using self.driver as the driver is present within the class
        homepage.shop_items().click()  # self.driver.find_element(By.LINK_TEXT, "Shop").click()
        checkoutpage = CheckoutPage(self.driver)
        Cards = checkoutpage.get_card_elements()  # self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        i = -1
        for card in Cards:
            i = i + 1
            productName = card.text
            if productName == "Samsung Note 8":
                checkoutpage.get_card_footer()[i].click()
                # self.driver.find_elements(By.CSS_SELECTOR(".card-footer button"))
        checkoutpage.get_checkout_btn().click()
        # self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()

        checkoutpage.get_sec_checkout_btn().click()
        # self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        self.driver.find_element(By.ID, "country").send_keys("Ind")

        confirm_page = ConfirmPage(self.driver)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

        confirm_page.get_country_name().click()
        # self.driver.find_element(By.LINK_TEXT, "India").click()

        confirm_page.get_purchase_btn().click()
        # self.driver.find_element(By.XPATH, "//input[@class='btn btn-success btn-lg']").click()

        success_msg = confirm_page.get_success_msg().text
        # self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text

        assert "Success! Thank you!" in success_msg