from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

fake = Faker()

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://practicetestautomation.com/practice-test-login/")

driver.find_element(By.ID, "username").send_keys(fake.user_name())
driver.find_element(By.ID, "password").send_keys(fake.password())

driver.find_element(By.ID, "submit").click()

error = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "error"))
)

assert "Your username is invalid!" in error.text

print("✅ Test Passed")

driver.quit()