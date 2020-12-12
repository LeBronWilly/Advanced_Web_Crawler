# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14

@author: Willy Fang

"""
#%%   <------劃分cell用的

# Selenium可以藉由指令自動操作網頁，達到測試的功能

from selenium import webdriver
from time import sleep

urls = ['http://www.google.com',
        "https://www.ba.ntust.edu.tw/cht/",
        'http://im.mgt.ncu.edu.tw/index/main.php',
        'https://facebook.com/',
        "https://github.com/LeBronWilly",] # 網址(URL)的清單(List)

#%%

browser = webdriver.Chrome() # 建立Google Chrome瀏覽器物件(browser)，以做後續的操縱
browser.maximize_window() # 瀏覽器視窗最大化

#%%

for url in urls:
    browser.get(url) # 連結網址(URL)
    sleep(2) # 給它一點時間跑，不要太快！

#%%

browser.close() # 關閉瀏覽器



#%%

# browser = webdriver.Firefox()

# pip install bs4 selenium openpyxl requests numpy pandas
