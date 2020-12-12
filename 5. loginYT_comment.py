# -*- coding: utf-8 -*-
"""
Created on Sun Nov 8

@author: Willy Fang

"""
#%%

from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
from openpyxl import Workbook # pip install openpyxl

url = 'https://www.youtube.com/watch?v=70RTxbhqj5s&list=RDR2V9sHAlLuQ&index=3'


# 宣告瀏覽器的options，取消Alert視窗
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)


#%%

browser = webdriver.Chrome(options=chrome_options) # 增加options參數
# browser.maximize_window()
browser.get(url)
sleep(2)

#%% 登入哦
# email="XXXXX@gmail.com"
# password="xxxxxx"

# browser.find_element_by_class_name('style-scope.ytd-masthead.style-suggestive.size-small').click()
# sleep(1.5)
# browser.find_element_by_id('identifierId').clear()
# browser.find_element_by_id('identifierId').send_keys(email)
# browser.find_element_by_class_name('VfPpkd-RLmnJb').click()
# sleep(1.5)
# browser.find_element_by_xpath("//input[@type='password']").clear()
# browser.find_element_by_xpath("//input[@type='password']").send_keys(password)
# browser.find_element_by_class_name('VfPpkd-RLmnJb').click()
# sleep(1.5)

#%%

# 因為有時YT會有多重廣告，所以多try幾次
try:
    try:
        browser.find_element_by_xpath("//button[@title='暫停 (k)']").click()
        print("1st成功暫停！")
    except:
        browser.find_element_by_xpath("//button[@title='Pause (k)']").click()
        print("1st Pause Success！")
except:
    print("1stOK")

sleep(1)

try:
    try:
        browser.find_element_by_xpath("//button[@title='暫停 (k)']").click()
        print("2nd成功暫停！")
    except:
        browser.find_element_by_xpath("//button[@title='Pause (k)']").click()
        print("2nd Pause Success！")
except:
    print("2ndOK")

# 建立往下滑動的funcation（使用javascript）
def scrolldown(times,height): # 設定參數（次數與滑動單位）
    c=450 # 首次先給他滑一點點zZ，這很重要，滑太多會抓不到，自己去拿捏哦
    for i in range(times):
        js = 'window.scrollBy(0,' + str(c) + ');'
        c=height # 恢復到最初設定的單位
        browser.execute_script(js)
        sleep(1.5)
scrolldown(7,20000) # height也是自己去拿捏哦


myExcel = Workbook() # 用python建立一個Excel空白活頁簿
sheet = myExcel.active # 建立一個工作中的表單
sheet['A1'] = 'Comments' # 填入第一列的欄位名稱

soup = BeautifulSoup(browser.page_source, "html.parser")
# comments = soup.find_all("yt-formatted-string", class_='style-scope ytd-comment-renderer', attrs={'id':'content-text'})
comments = soup.select("#content-text")
comments_list = comments.copy() # 可以額外copy一份，能夠以免動到原本的
for i in comments:
    print(i.text)
    print()
    sheet.append([i.text])
myExcel.save('YTcomments.xlsx')

try:
    try:
        browser.find_element_by_xpath("//button[@title='暫停 (k)']").click()
        print("3rd成功暫停！")
    except:
        browser.find_element_by_xpath("//button[@title='Pause (k)']").click()
        print("3rd Pause Success！")
except:
    print("3rdOK")



#%%

# 參考資料（並非都有使用到）：
# https://pydoing.blogspot.com/2011/01/python-try.html
# http://hk.uwenku.com/question/p-qkncjsjr-nm.html
# https://mlog.club/article/2332546
# https://www.shuzhiduo.com/A/ke5jLokXzr/
# https://qa.1r1g.com/sf/ask/703061131/
# https://blog.techbridge.cc/2018/10/05/how-to-use-python-manipulate-excel-spreadsheet/
# https://newaurora.pixnet.net/blog/post/228244997-python-%E8%B3%87%E6%96%99%E5%AD%98%E6%88%90excel%E6%AA%94


# firefox_options = webdriver.FirefoxOptions()
# browser = webdriver.Firefox(options=firefox_options)
# firefox_options.set_preference("profile.default_content_setting_values.notifications",2)
