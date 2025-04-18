from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://localhost:5000")
assert "Hello" in driver.page_source
driver.quit()
