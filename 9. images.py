# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 01:40:26 2020

@author: Willy Fang

"""
#%%

import os
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://www.zara.com/tw/zt/search'

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

#%%


def scrolldown(times, height): # 設定參數（次數與滑動單位）
    for i in range(times):
        js = 'window.scrollBy(0,' + str(height) + ');'
        browser.execute_script(js)
        sleep(0.1)

keyword="褲子"

browser = webdriver.Chrome(options=chrome_options)
# browser.maximize_window()
browser.get(url)
sleep(2)

browser.find_element_by_id('search-term').send_keys(keyword)
sleep(2)

try:
    browser.find_element_by_partial_link_text("女士").click()
    sleep(1)
    scrolldown(200,100)
    # scrolldown(100,150)
    a = browser.page_source
except:
    pass
# sleep(15)

soup = BeautifulSoup(browser.page_source, "html.parser") # 用browser.page_source取得網頁原始碼，並且用BeautifulSoup解析

#%%

# js = "window.scrollTo(0, document.body.scrollHeight);"
# for i in range(1,101):
#     # 向下捲動，會花費一些時間
#     browser.execute_script(js)
#     sleep(0.3)


# soup=BeautifulSoup(browser.page_source,'html.parser')  
# title = soup.select('.album-title')[0].text.strip()   # 標題
# all_imgs = soup.find_all('img', 
#                           {"class": "photo_img photo-img"})


# # 以標題建立目錄儲存圖片
# images_dir=title + "/"
# if not os.path.exists(images_dir):
#     os.mkdir(images_dir)


# # 處理所有 <img> 標籤
# n=0

# for img in all_imgs:
#     # 讀取 src 屬性內容
#     src=img.get('src')

#     # 讀取 .jpg 檔
#     if src != None and ('.jpg' in src):
#         # 設定圖檔完整路徑
#         full_path = src            
#         filename = full_path.split('/')[-1]  # 取得圖檔名
#         print(full_path)

#         # 儲存圖片
#         try:
#             image = urlopen(full_path)
#             with open(os.path.join(images_dir,
#                                     filename),'wb') as f:
#                 f.write(image.read())  
#             n+=1
#             if n>=1000: # 最多下載 1000 張
#                 break
#         except:
#             print("{} 無法讀取!".format(filename))


# print("共下載",n,"張圖片")
# browser.quit(); # 關閉瀏覽器並退出驅動程式