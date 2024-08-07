from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):  # using inheritance, we are inheriting the fixture properties of the BaseClass for
    # more code readability, now we need not define the fixture redundant code
    def test_e2e(self):  # here self is already loaded with the driver variable which was defined in the setup fixture,
        # so we don't need to add the setup parameter in this method
        self.driver.implicitly_wait(4)
        self.driver.find_element(By.LINK_TEXT, "Shop").click()
        Cards = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        for card in Cards:
            productName = card.find_element(By.XPATH, "div/h4/a").text
            if productName == "Samsung Note 8":
                card.find_element(By.XPATH, "div/button").click()

        self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        self.driver.find_element(By.ID, "country").send_keys("Ind")

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

        self.driver.find_element(By.LINK_TEXT, "India").click()

        self.driver.find_element(By.XPATH, "//input[@class='btn btn-success btn-lg']").click()
        assert "Success! Thank you!" in self.driver.find_element(By.XPATH, "//div[@class='alert alert-success "
                                                                           "alert-dismissible']").text
