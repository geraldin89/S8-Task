from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

# Open the Urban Routes home page
driver.get (" https://cnt-3ba3bed8-2505-4488-bf39-4a2705f29fb1.containerhub.tripleten-services.com")

# Check url contains tripleten-services.com
assert "tripleten-services.com" in driver.current_url

# Close the browser
driver.quit ()