# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 01:51:33 2020

@author: Willy Fang
# 講解方法+自由操作
"""
#%%

import requests
from time import sleep
from bs4 import BeautifulSoup


# 建立一個單頁PTT爬蟲函數
def get_PTT_onepage(URL): # 參數是一個網址字串
    my_headers = {'cookie': 'over18=1;'} # 設定Header與Cookie
    ptt_html = requests.get(URL, headers = my_headers) # 發送get請求到PTT版
    pttbs4 = BeautifulSoup(ptt_html.text, "html.parser") # 解析HTML
    # 由於.select()會回傳List，需要使用for迴圈將逐筆取出
    for t in pttbs4.select(".title a"):
        print(t.string) # 把各標籤的文字內容萃取出來
        PTT_multipages_titles.append(t.string)



#%%

start = 2130 # 設定起始頁（自行調整）
number = 10 # 設定要往前或往後爬多少頁（自行調整，會包含起始頁）
# end = start - number   # 往前爬
end = start + number  # 往後爬

#%%

# PTTgraduate版：https://www.ptt.cc/bbs/graduate/index.html

PTT_multipages_titles = []

# for i in range(start,end,-1): # 往前爬
for i in range(start,end,1): # 往後爬
    # 組合URL，這概念在下個爬取【Google Maps評論】會用到喔喔喔
    link = "https://www.ptt.cc/bbs/graduate/index"+str(i)+".html"
    print("\n==============第",i,"頁==============")
    get_PTT_onepage(link) # 執行單頁PTT爬蟲
    sleep(1) # 每次休息1秒