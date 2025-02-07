from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


url = "https://www.instagram.com/guviofficial/"
driver.get(url)


time.sleep(5)


followers = driver.find_element(By.XPATH, "//ul/li[1]/div/span/span").text
following = driver.find_element(By.XPATH, "//ul/li[3]/div/span/span").text

print(f"Followers: {followers}")
print(f"Following: {following}")

driver.quit()
