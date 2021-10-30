#!/usr/bin/env python
# coding: utf-8

# In[167]:


import pyautogui
from PIL import Image, ImageGrab
from PIL import ImageOps
from PIL import Image
import time


# In[254]:


def isCollision(data):
    if data[1170, 1145] == 0: # middle board
        for y in range(200, 850):# middle box
            if data[1139, y] < 185 and data[1139, y] != 213 and data[1139, y] != 214 and data[1139, y] != 212:
                pyautogui.press('left')
                return
    if data[900, 1145] == 0: #left board
        for y in range(200, 850): #left box
            if data[875, y] < 185 and data[1139, y] != 213 and data[1139, y] != 214 and data[1139, y] != 212:
                pyautogui.press('right')
                return

if __name__ == "__main__":
    time.sleep(3)
    pyautogui.click(x = 1130, y=950)

while True: 
    image = ImageGrab.grab().convert("L")
    data = image.load()
    isCollision(data)
    pyautogui.click(x = 1130, y=950)
    
    '''for x in range(1110,1160): # middle board
        for y in range(1000, 1010):
            data[x, y] = 0
    for x in range(1390,1420): # right box
        for y in range(10, 1015):
            data[x, y] = 0
    for x in range(850,875): #left box
        for y in range(1015, 1030):
            data[x, y] = 0'''


# In[204]:


time.sleep(2)
pyautogui.position()


# In[244]:


time.sleep(2)

image = ImageGrab.grab().convert('L')
#inverted = ImageOps.invert(image)
data = image.load()

'''for x in range(900,903): #left board
    for y in range(1145, 1150):
        data[x, y] = 50
for x in range(1537,1539): # right box
    for y in range(200, 450):
        data[x, y] = 150
for x in range(995,1198): #middle box
    for y in range(450, 800):
        data[x, y] = 160
for x in range(1170,1174): # middle board
    for y in range(1145, 1150):
        data[x, y] = 171
for x in range(1433,1439): # right board
    for y in range(1145, 1150):
        data[x, y] = 190
for x in range(1017,1019): #left box
    for y in range(450, 800):
        data[x, y] = 200'''
for x in range(1139, 1144):
    for y in range(1000, 1100):
        data[x,y] = 212
data[875, 600] = 0
image.show()


# In[234]:


time.sleep(2)
image = ImageGrab.grab().convert("L")
    #inverted = ImageOps.invert(image)
data = image.load()
image.show()
im1 = Image.Image.getcolors(image)
print(im1)


# In[231]:


def isCollision(data):
    if data[1170, 1145] == 0: # middle board
        for y in range(200, 850):# middle box
            if data[1196, y] > 150:
                pyautogui.press('left')
                return

    if data[1433, 1145] == 0: #right board
            for y in range(200, 850): #right box
                if data[1337, y] > 150:
                    pyautogui.press('left')
                    return

    if data[900, 1145] == 0: #left board
        for y in range(200, 850): #left box
            if data[817, y] > 150:
                pyautogui.press('right')
                return


# In[ ]:


''' if data[1433, 1145] == 0: #right board
            for y in range(200, 850): #right box
                if data[1376, y] < 185:
                    pyautogui.press('left')
                    return'''


# In[ ]:




