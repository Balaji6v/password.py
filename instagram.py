from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up the WebDriver in headless mode
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the Instagram page
url = "https://www.instagram.com/guviofficial/"
driver.get(url)


time.sleep(5)

try:

    followers = driver.find_element(By.XPATH, "//ul/li[1]/div/span/span").text
    following = driver.find_element(By.XPATH, "//ul/li[3]/div/span/span").text


    print(f"Followers: {followers}")
    print(f"Following: {following}")

except Exception as e:
    print("Error:", e)


driver.quit()
