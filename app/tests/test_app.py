from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Set Chrome to run in headless mode for CI environments
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the local web app
driver.get("http://localhost:5000")

# Assert page contains "Hello"
assert "Hello" in driver.page_source

# Quit driver
driver.quit()
