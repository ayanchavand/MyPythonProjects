from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)  

driver.get("https://web.whatsapp.com") #get on the website
print("Opening whatsApp web...")

time.sleep(10)
print("You have 10 seconds to scan!")

username = str(input())
print("Messaging "+ username + "!")

user = driver.find_element_by_xpath('//span[@title="{}"]'.format(username)) #finding user by the name
user.click()

time.sleep(1) #JTMS

message_box = driver.find_element_by_xpath('//div[@class="_3uMse"]') #find the messaging box
message_box.send_keys("haha lol, This message was sent by BOT") #message
message_box.send_keys(Keys.RETURN)

print("Message sent sucessfully!")

