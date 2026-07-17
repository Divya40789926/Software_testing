from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

driver.find_element(By.NAME, "my-text").send_keys("Divya")
driver.find_element(By.NAME, "my-password").send_keys("password123")
driver.find_element(By.NAME, "my-textarea").send_keys("Testing Selenium")

Select(driver.find_element(By.NAME, "my-select")).select_by_index(1)

driver.find_element(By.CSS_SELECTOR, "button").click()

WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element(
        (By.TAG_NAME, "h1"),
        "Form submitted"
    )
)

print("✅ Test Passed")

driver.quit()