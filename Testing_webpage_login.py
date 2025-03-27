from selenium import webdriver  
#webdriver used to control the browser
from selenium.webdriver.common.by import By   
#By used to locate the given web elements 
from selenium.webdriver.support.ui import WebDriverWait  
#Used for waiting until an element is available/loaded
from selenium.webdriver.support import expected_conditions as EC    
#Expected conditions (EC) Contains conditions like element visibility, clickability, etc.

#if u need to externally specify the path of the browser driver then u need to use
#service_obj=Service("/path/boweser_driver")
#driver_chrome=webdriver.Chrome(service_obj)

# Launch browser
driver_chrome = webdriver.Chrome()
driver_chrome.get("https://opensource-demo.orangehrmlive.com/")

# Explicit wait for username field
wait = WebDriverWait(driver_chrome, 5)
username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
#checking if the element is available or not and max time to wait is 5 sec
#DOM - Document Object Model is a structural representation of a HTML page.

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
