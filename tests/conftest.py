import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


# https://docs.pytest.org/en/7.1.x/example/simple.html

# defining command line arguments
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Options: chrome or firefox or edge"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        service_obj = Service(r"C:\Users\shubhangvats\OneDrive - Hexaview Technologies\Downloads\chromedriver-win64"
                              r"\chromedriver-win64\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver  # here we are tying up the request instance of this fixture to class instance (driver)
    # which will use this fixture
    yield
    driver.close()

# we cannot use return and yield keywords together, so to overcome that, we define the instance "request" which is
# available for fixtures in the setup method and using that we set the class variable as the required value,
# then we use yield
