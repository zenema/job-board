from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.metajob.de/it")
assert "metajob" in driver.title
# driver.close()