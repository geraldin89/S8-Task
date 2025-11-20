import time

from selenium.webdriver.common.by import By
from selenium import webdriver


# Initialize a new instance of the Chrome WebDriver
driver = webdriver.Chrome()

# Open the specified URL in the browser
driver.get(" https://cnt-be8b9974-e89a-45f9-926b-0982bb63ef52.containerhub.tripleten-services.com")

# Pause execution for 2 seconds to allow the page to load fully
time.sleep(2)

# Find the FROM input field and TO input field using their IDs
from_field = driver.find_element(By.ID, "from")
to_field = driver.find_element(By.ID, "to")

# Test the placeholder attribute for each input field to ensure they display the correct text
assert from_field.get_attribute('placeholder') == "East 2nd Street, 601"
assert to_field.get_attribute('placeholder') == "1300 1st St"

# Close the browser and end the WebDriver session
driver.quit ()
