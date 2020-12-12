# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15

@author: Willy Fang

"""

'''
後面的文字處理做法不完美，除了分段外，特別是處理"See More"的解方目前也無，有興趣的同學可以研究如何去改善，或是去研究FB的Facebook圖形API(Facebook for developers)及Facebook-SDK的使用為何

'''

#%%
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

url = 'https://www.facebook.com/'
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

#%%

email="xxx@gmail.com"
password="xxx"

browser = webdriver.Chrome(options=chrome_options)
browser.get(url)

browser.find_element_by_id('email').send_keys(email)
browser.find_element_by_id('pass').send_keys(password)
sleep(1.5)
browser.find_element_by_xpath("//button[@value='1']").click() # 按登入
sleep(1.5)
browser.get("https://www.facebook.com/%E5%BF%97%E7%A5%BA%E4%B8%83%E4%B8%83-231881397571066/")
sleep(1.5)

# 建立往下滑動的funcation（使用javascript）
def scrolldown(times):# scrolltimes代表頁面滾動的次數
    for i in range(times):
        if i == 0: # 當瀏覽器跑比較慢時，若一次拉到底會讀不到東西
            js = 'window.scrollBy(0,3000);' # 要自己去拿捏
        else:
            js = 'window.scrollBy(0, document.body.clientHeight);'
        browser.execute_script(js) # 在目前的視窗畫面，執行javascript，使得每一次滑動都是滑到瀏覽器網頁的最下方
        sleep(1.5)


# 呼叫function就會直接滾動頁面
scrolldown(3) # 設定參數，即為滑到底的次數


sleep(1.5)
soup = BeautifulSoup(browser.page_source, "html.parser")
contents = soup.find_all(class_='d2edcug0 hpfvmrgz qv66sw1b c1et5uql rrkovp55 a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v knj5qynh oo9gr5id hzawbc8m')

contents_list=[]
for i in contents:
    contents_list.append(i.text)

# 文字處理做法不完美，除了分段外，特別是處理"See More"的解方目前也無，有興趣的同學可以研究如何去改善，或是去研究FB的Facebook圖形API(Facebook for developers)及Facebook-SDK的使用為何
# print(contents_list) # 可以看到從第5個開始，才是我們所要的東西

#%%

# 參考資料（並非都有使用到 or 在這裡使用到）：
# https://dotblogs.com.tw/aquarius6913/2011/01/03/20538
# https://developer.mozilla.org/en-US/docs/Web/API/Window/scrollTo
# https://www.itread01.com/content/1550041766.html
# https://www.itread01.com/content/1558922582.html




# firefox_options = webdriver.FirefoxOptions()
# firefox_options.set_preference("profile.default_content_setting_values.notifications",2)
# browser = webdriver.Firefox(options=firefox_options)
# browser.maximize_window()

# browser.find_element_by_xpath("//div[@class='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p']").click()
