from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
#get on the website
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(10)

cookie = driver.find_element_by_id("bigCookie")
cookie_num = driver.find_element_by_id("cookies")

items = [ driver.find_element_by_id("productPrice" + str(i)) for i in range (1,-1,-1)]


actions = ActionChains(driver)
actions.click(cookie)
for f in range(500):
    actions.perform()