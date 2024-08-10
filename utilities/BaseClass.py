import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import inspect
import logging


@pytest.mark.usefixtures("setup")  # browser invocation is defined as fixture, for reducibility
class BaseClass:
    def verify_link_presence(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def select_dd_value(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def get_logger(self):
        logger_name = inspect.stack()[1][3]  # this is done to get the name of the method, from where the test ran
        logger = logging.getLogger(logger_name)
        fileHandler = logging.FileHandler('logfile.log')

        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)

        return logger
