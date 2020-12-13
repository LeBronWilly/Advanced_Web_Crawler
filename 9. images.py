# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 01:40:26 2020

@author: Willy Fang
# 講解方法+自由操作
"""
#%%

import os, requests
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup

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

keyword="裙子"

browser = webdriver.Chrome(options=chrome_options)
# browser.maximize_window()
browser.get(url)
sleep(2)
browser.find_element_by_id('search-term').send_keys(keyword)
sleep(2)


#%%

# 女士
try:
    browser.find_element_by_partial_link_text("女士").click()
    sleep(1)
    scrolldown(50,80) # 自己去調整
    sleep(2)
    lady_soup = BeautifulSoup(browser.page_source, "html.parser")
    # 這裡的select稍微複雜
    lady_images = lady_soup.select("img[src].media-image__image.media__wrapper--media")
    
    lady_images_dir= "Lady/"
    if not os.path.exists(lady_images_dir):
        os.mkdir(lady_images_dir)
    
    for img in lady_images:
        src = img.get("src") # 也可以寫src = img["src"]
        if ".jpg" in src:
            full_path = src
            filename = src.split("/")[-1].split("?")[0]
            # print(src)
            try:
                print("Downloading......")
                image = requests.get(full_path)
                with open(os.path.join(lady_images_dir,filename),"wb") as f:
                    f.write(image.content)
                print("Done!")
                # sleep(0.5)
            except:
                print("{} can't be read!".format(filename))
        else:
            print("Not jpg")
except:
    print("No Lady!")



# 男士





# 童裝






#%%


# https://www.learncodewithmike.com/2020/09/download-images-using-python.html
# https://ithelp.ithome.com.tw/articles/10211545

# print("共下載",n,"張圖片")
# browser.quit(); # 關閉瀏覽器並退出驅動程式