import time

from selenium.webdriver.common.by import By
from selenium import webdriver


# Initialize a new instance of the Chrome WebDriver
driver = webdriver.Chrome()

# Open the specified URL in the browser
driver.get("https://cnt-2a2f7709-5c02-4494-a978-6c483c8af94b.containerhub.tripleten-services.com")


# Pause execution for 2 seconds to allow the page to load fully
time.sleep(2)

# Find the title element using its CSS Selector
driver.find_element(By.CSS_SELECTOR, ".logo-disclaimer")

# Close the browser and end the WebDriver session
driver.quit ()
