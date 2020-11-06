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
#what's the title
print(driver.title)
#find stuff with the name s
search = driver.find_element_by_name("s")
#type test
search.send_keys("test")
#hit enter
search.send_keys(Keys.RETURN)


try:
    #wait until the search loades
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    #print the text from the main element
    print(main.text)
except:
    driver.quit()

driver.quit()

