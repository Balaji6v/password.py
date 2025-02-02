from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Path to ChromeDriver executable
driver_path = ("C:\\Windows\\chromedriver-win64\\chromedriver.exe")
service = Service(driver_path)

# Initialize the WebDriver
driver = webdriver.Chrome(service=service)

try:
    # Open the SauceDemo website
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    # Log in to the site
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button.click()

    # Wait for the page to load
    time.sleep(3)

    # Print the page title
    print("Page Title:", driver.title)

    # Find and print product names
    products = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    print("Available Products:")
    for product in products:
        print("-", product.text)

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the browser
    driver.quit()


