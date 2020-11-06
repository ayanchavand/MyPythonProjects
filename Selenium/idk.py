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
driver.get("https://techwithtim.net")

try:
    #wait until the search loades
    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.LINK_TEXT,"Django Tutorial"))
    )
    element.click()
    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID,"sow-button-19310003"))
    )
    element.click()
    
except:
    input()
    driver.quit()


#driver.quit()

