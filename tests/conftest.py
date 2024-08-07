import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def setup(request):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    service_obj = Service(r"C:\Users\shubhangvats\OneDrive - Hexaview Technologies\Downloads\chromedriver-win64"
                          r"\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj, options=chrome_options)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver  # here we are tying up the request instance of this fixture to class instance (driver)
    # which will use this fixture
    yield
    driver.close()

# we cannot use return and yield keywords together, so to overcome that, we define the instance "request" which is
# available for fixtures in the setup method and using that we set the class variable as the required value,
# then we use yield
