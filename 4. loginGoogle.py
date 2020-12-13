# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10

@author: Willy Fang

"""
#%%

from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

### 變數宣告
url = 'http://www.google.com'
email="XXXXX@gmail.com"
password="xxxxxx"
keyword="NTUST BA"


#%% 定位初始網頁

browser = webdriver.Chrome() # 此時Chrome將被自動打開
browser.get(url)
sleep(1.5)


#%% 取得HTML網頁元素的方法
# 取得第一個符合的元素
'''browser.find_element_by_xxxxx()，跟上週教的soup.find()方法很類似

1. find_element_by_id()：用id屬性查詢符合的元素
2. find_element_by_class_name()：用class屬性查詢符合的元素（class屬性若有空格要加.）
3. find_element_by_link_text()：用超連結的文字查詢符合的元素
4. find_element_by_partial_link_text()：用超連結的部分文字查詢符合的元素
5. find_element_by_xpath()：以XML的路徑查詢（全名為XML Path），XPath是利用節點的樹狀關係，以及每個節點的特性來查詢符合的元素（簡單來說，類似就是利用絕對位置及相對位置去找，也可以用手刻的，方便使用但有機率會抓失敗）
PS. Chrome可以下載擴充套件ChroPath，輕鬆取得XPath

6. find_element_by_tag_name()：用標籤名稱查詢符合的元素
7. find_element_by_name()：用name屬性查詢符合的元素
8. find_element_by_css_selector()：用css選擇器定位（高階使用，比較難操作）

PS. 若element加個s，則會是取得所有符合的元素，跟上週教的soup.find_all()或soup.select()方法很類似
'''
#%% 登入Google帳密

browser.find_element_by_id('gb_70').click() # 按右上角的登入鈕
sleep(1.5)

browser.find_element_by_id('identifierId').send_keys(email) # 輸入帳號
sleep(1.5)

browser.find_element_by_class_name("VfPpkd-RLmnJb").click() # 按繼續鈕
sleep(1.5)

browser.find_element_by_class_name("whsOnd.zHQkBf").send_keys(password) # 輸入密碼
sleep(1.5)

browser.find_element_by_class_name("VfPpkd-RLmnJb").click() # 按 繼續鈕
sleep(1.5)


#%% 搜尋引擎-關鍵字搜尋

browser.find_element_by_class_name("gLFyf.gsfi").send_keys(keyword)
# browser.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input").send_keys(keyword) ### 使用相對Xpath
# browser.find_element_by_xpath("/html/body/div[2]/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input").send_keys(keyword) ### 使用絕對Xpath
# browser.find_element_by_xpath("//input[@class='gLFyf gsfi']").send_keys(keyword) ### 自己判斷手打(其實這個算蠻好用的)
sleep(1.5)

browser.find_element_by_class_name("gNO89b").click()
sleep(1.5)

### 定位目標網頁
browser.find_element_by_partial_link_text("台科大").click()
sleep(1)

try:
    browser.switch_to.window(browser.window_handles[1]) ### 切換Chrome分頁
    sleep(1.5)
except:
    pass

# browser.find_element_by_xpath("/html/body/div/header/div/div[2]/div/div/div[1]/div/div/div/nav/ul/li[2]/a/span").click()
# browser.find_element_by_class_name("nav-link").click()
browser.find_element_by_link_text("師資陣容").click()
sleep(1.5)

browser.find_element_by_link_text("林孟彥").click()
sleep(1.5)


#%% 爬取資料並輸出

soup = BeautifulSoup(browser.page_source, "html.parser") # 用browser.page_source取得網頁原始碼，並且用BeautifulSoup解析
lin_list = soup.select("div #a1 tbody tr")

# lin_list_copy = lin_list.copy() # 可以額外copy一份，能夠以免動到原本的

for i in lin_list[1:]:
    for j in i.select("td"):
        print()
        print(j.string)


#%%


# browser = webdriver.Firefox（）

