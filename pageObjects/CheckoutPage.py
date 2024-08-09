from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:
    card_element = (By.XPATH, "//div[@class='card h-100']")
    card_name = (By.XPATH, "//div[@class='card h-100']/div/h4/a")
    card_footer = (By.CSS_SELECTOR, ".card-footer button")
    checkout_btn = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    sec_checkout_btn = (By.XPATH, "//button[@class='btn btn-success']")


    def __init__(self, driver):
        self.driver = driver

    def get_card_elements(self):
        return self.driver.find_elements(*CheckoutPage.card_element)

    def get_card_footer(self):
        return self.driver.find_element(*CheckoutPage.card_footer)

    def get_checkout_btn(self):
        return self.driver.find_element(*CheckoutPage.checkout_btn)

    def get_sec_checkout_btn(self):
        self.driver.find_element(*CheckoutPage.sec_checkout_btn).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page

