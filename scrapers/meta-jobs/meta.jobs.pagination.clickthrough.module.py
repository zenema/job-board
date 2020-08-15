from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Init
options = webdriver.ChromeOptions()

# Uncomment these lines to run in headless mode
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')


driver = webdriver.Chrome(options=options)
driver.wait = WebDriverWait(driver, 10)
driver.get("https://www.metajob.de/it")
# assert "metajob" in driver.title



# Get to next page
# next_page_button = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div[1]/div[2]/ul/li[10]/button")
# next_page_button.click()

    # driver.close()