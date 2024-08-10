import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

driver = None


# https://docs.pytest.org/en/7.1.x/example/simple.html

# defining command line arguments
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Options: chrome or firefox or edge"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
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


# this is a copied and pasted code
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
