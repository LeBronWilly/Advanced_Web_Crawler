# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14

@author: Willy Fang
# 講解方法
"""
#%%
from selenium import webdriver
from time import sleep

url = 'https://opendata.epa.gov.tw/Data/Contents/AQI/'

#%%

browser = webdriver.Chrome()
#browser = webdriver.Firefox()
# browser.maximize_window()
browser.get(url)

#sleep(3)  # 必須加入等待，否則會有誤動作
#browser.find_element_by_link_text("空氣品質即時污染指標").click()

sleep(2)  # 必須加入等待，否則會有誤動作
browser.find_element_by_link_text("JSON").click() # 讀取json

sleep(2)  # 必須加入等待，否則會有誤動作
browser.find_element_by_link_text("XML").click() # 讀取XML

sleep(2)  # 必須加入等待，否則會有誤動作
browser.find_element_by_link_text("CSV").click() # 下載csv

#browser.close()