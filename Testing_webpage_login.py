from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch browser
driver_chrome = webdriver.Chrome()
driver_chrome.get("https://opensource-demo.orangehrmlive.com/")

# Explicit wait for username field
wait = WebDriverWait(driver_chrome, 10)
username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))

# Enter credentials
username_field.send_keys("Admin")
driver_chrome.find_element(By.NAME, "password").send_keys("admin123")
driver_chrome.find_element_by_name()
# Click the login button
login_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "orangehrm-login-button")))
login_button.click()

# Optional: Wait before closing to see the result
import time
time.sleep(5)

act_title=driver_chrome.title
exp_title="OrangeHRM"

if act_title == exp_title:
    print("Title test is passed")
else:
    print("Login test Failed")

# Close browser
driver_chrome.close()
