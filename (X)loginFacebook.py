# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14

@author: Willy Fang

"""
#%%

from selenium import webdriver
from time import sleep

# FB首次登入時會出現Alert視窗
url = 'https://www.facebook.com/'

# 取消Alert視窗
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs", prefs)

#%%

browser = webdriver.Chrome(options=chrome_options)
browser.get(url)

# 不斷地定位網頁HTML元素
# find_element:抓取第一個符合ㄉ
# find_elements:抓取所有符合ㄉ

email="w70024@gmail.com"
password="lebron230613"

browser.find_element_by_id('email').clear()
browser.find_element_by_id('email').send_keys(email)
browser.find_element_by_id('pass').clear()
browser.find_element_by_id('pass').send_keys(password)
sleep(1.5)
# browser.find_element_by_xpath("//button[@value='1']").click() # 按登入
browser.find_element_by_id("u_0_b").click() # 按登入
sleep(1.5)
browser.get("https://www.facebook.com/me/") # 到自己的主頁
sleep(3)
browser.back() # 回上一頁
sleep(1.5)
browser.forward() # 回下一頁


sleep(1.5)
browser.get("https://www.facebook.com/靠北中央-1514597625469099/")
sleep(2)
browser.get("https://www.facebook.com/志祺七七-231881397571066/")
sleep(2)
browser.get("https://www.facebook.com/chuchushoeTW")


#%%

# browser.maximize_window()
# firefox_options = webdriver.FirefoxOptions()
# browser = webdriver.Firefox(options=firefox_options)
# firefox_options.set_preference("profile.default_content_setting_values.notifications",2)


