from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.demoblaze.com/")
time.sleep(2)

driver.find_element(By.LINK_TEXT,"Laptops").click()
time.sleep(3)

products = driver.find_elements(By.CLASS_NAME,"card-title")

print("Laptop Products")

for p in products:
    print(p.text)

driver.quit()