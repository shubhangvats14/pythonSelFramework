from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service_obj = Service(r"C:\Users\shubhangvats\OneDrive - Hexaview Technologies\Downloads\chromedriver-win64"
                      r"\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.get("https://rahulshettyacademy.com/upload-download-test")
driver.implicitly_wait(5)
driver.find_element(By.ID, "downloadButton").click()
upload_btn = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
upload_btn.send_keys(r"C:\Users\shubhangvats\OneDrive - Hexaview Technologies\Downloads\download.xlsx")

toast_locator = (By.CSS_SELECTOR, ".Toastify__toast-body div:nth-child(2)")
column_name = 'Price'
fruit = 'Apple'
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(toast_locator))
print(driver.find_element(*toast_locator).text)
column = driver.find_element(By.XPATH, "//div[text()='"+column_name+"']").get_attribute("data-column-id")
# Here we have used the column_name variable to generalize the column in order to get the locator for any column
# when the locator is reached to the column, we brought the value of "data-column-id", which is the index of the row

actual_price = driver.find_element(By.XPATH, "//div[text()= '"+fruit+"']/parent::div/parent::div/"
                                                                     "div[@id='cell-"+column+"-undefined']").text
# Here we are using the parent traversal, as we traversed from Apple to the parent div(s) togs
# Now, using the fruit name and the column index, we brought the value on the cell

print(actual_price)

driver.close()


