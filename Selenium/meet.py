#imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#the path of driver
path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
#get on the website
driver.get("https://meet.google.com")

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME,"VfPpkd-RLmnJb"))
    )
    main.click()
except:
    driver.quit()
    