from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

fake = Faker()

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://practice.expandtesting.com/register")

# Generate valid test data
username = fake.user_name()
password = fake.password(length=12, special_chars=True)

# Fill all required fields
driver.find_element(By.ID, "username").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.ID, "confirmPassword").send_keys(password)

# Click Register
submit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
)

driver.execute_script("arguments[0].click();", submit_button)

print("Registration form submitted successfully!")

driver.quit()