import pyautogui
from PIL import Image, ImageGrab 
import time

def hit(key):
    pyautogui.keyDown(key)

def screen():
    image = ImageGrab.grab().convert('L')
    return image 

time.sleep(3)
image = screen() 
data = image.load()
for i in range(270, 350):
    for j in range(400, 430):
         data[i,j]=0

image.show()

