# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 

@author: Willy Fang

"""
#%% 前置作業

# 許多網頁中的資料是以XMLHttpRequest(XHR)的方式載入的(內容是json檔)，讓頁面能在不刷新的狀況下更新資料，所以要如何找到頁面XHR來源並進行爬取就十分重要(Request URL)


import requests, json
from openpyxl import Workbook # pip install openpyxl
import pandas as pd

# Google Maps超連結：國立中央大學-所有評論：
# https://www.google.com/maps/place/國立中央大學/@24.9678305,121.1927946,17z/data=!4m7!3m6!1s0x0:0xcdc129d4455ce456!8m2!3d24.9678305!4d121.1949833!9m1!1b1

# 可以發現Google Maps的評論的每一個XHR的Request URL都是有結構化的
url_a = 'XXX' # Request URL的上半
url_b = 'XXX' # Request URL的下半


# 每一個Request URL即代表一個XHR
# 每一個XHR會儲存10則評論(型態為json)
# Request URL中間的num就是表示從此數開始，抓往後10則評論(Ex. 8-->8~17、0-->0~9)進XHR中


#%% 爬取評論資料並儲存成List

comment_list = []
num = 0 # 負責用來中間拼湊完整的URL(這個可以不用宣告起來)
# 由於它每一個XHR本身一次就是抓10則評論，因此step參數即設為10
for num in range(0, 30, 10): # 會跑num = 0、10、20的迴圈
    # 組合成完整的URL，並發送get請求
    original_text = requests.get(url_a + str(num) + url_b).text 
    # 以下為資料處理original_text
    special_char = ')]}\'' # 特殊字元
    # 拿掉特殊字元，這個字元是為了資安而設定的
    text = original_text.replace(special_char,'')
    soup = json.loads(text) # 把字串轉換成json的資料格式
    comment_list.extend(soup[2]) # 擷取第2個（有包含留言的List）

# original_text


#%% 輸出資料

# 逐筆抓出
c = 1 # 用來標註評論的次序編號
for i in comment_list:  # 針對此維度的每一筆資料進行個別擷取
    # 每個i都是個多維度的List
    print("【" + str(c) + "】")
    print("Username: " + str(i[0][1]))
    print("User's Website: " + str(i[0][0]))
    print("Rate: " + str(i[4]) + "／5")
    print("Comment: " + str(i[3]))
    print("Time: " + str(i[1]))
    
    if i[14] != None:
        s = 1 # 用來標註圖片的次序編號
        for j in range(len(i[14])):
            print("⭐Photo " + str(s) +  ": "  + str(i[14][j][6][0]))
            s+=1
    else:
        print("Photo: " + str(i[14])) # 這裡str(i[14])會是None
    print("\n============蹦來個蹦蹦============")
    c+=1


#%% 資料寫入Excel(使用openpyxl)

myExcel = Workbook() # 用python建立一個Excel空白活頁簿
sheet = myExcel.active # 建立一個工作表
sheet['A1'] = 'No.' # 填入第一列的欄位名稱
sheet['B1'] = 'UserName'
sheet['C1'] = 'Rate'
sheet['D1'] = 'Comment'
sheet['E1'] = 'Time'
sheet['F1'] = 'Photo'


c = 1 # 用來標註評論的次序編號
for i in comment_list: # 針對此維度的每一筆資料進行個別擷取
    photo_list = [] # 先用來佔存圖片網址而用的
    if i[14] != None:
        for j in range(len(i[14])):
            photo_list.append(str(i[14][j][6][0]))
        sheet.append([str(c),
                      str(i[0][1]),
                      str(i[4]),
                      str(i[3]),
                      str(i[1]),
                      str(photo_list).strip("[]")])

    else:
        sheet.append([str(c),
                      str(i[0][1]),
                      str(i[4]),
                      str(i[3]),
                      str(i[1]),
                       "None"])
    c+=1

myExcel.save('XXGoogleMaps_comments1.xlsx')


#%% 資料寫入Excel(使用pandas)

data = []
columns = ["UserName","Rate","Comment","Time","Photo"] # DataFrame的第一列會預設index，因此這裡不多加編號No.

for i in comment_list: # 針對此維度的每一筆資料進行個別擷取
    photo_list = []
    if i[14] != None:
        for j in range(len(i[14])):
            photo_list.append(str(i[14][j][6][0]))
    data.append([str(i[0][1]), 
                 str(i[4]), 
                 str(i[3]), 
                 str(i[1]), 
                 str(photo_list).strip("[]")])


df = pd.DataFrame(data, columns=columns) # DataFrame的第一列會預設index
df.to_excel("XXGoogleMaps_comments2.xlsx")


#%% 參考資料（並非都有使用到 or 在這裡使用到）

# https://eyesofkids.gitbooks.io/javascript-start-from-es6/content/part4/ajax_fetch.html
# https://www.mdeditor.tw/pl/pKij/zh-tw
# https://limitedcode.blogspot.com/2014/01/xmlhttprequest.html
# https://medium.com/@bob800530/selenium-1-%E9%96%8B%E5%95%9Fchrome%E7%80%8F%E8%A6%BD%E5%99%A8-21448980dff9
# https://medium.com/@zx2515296964/python教學-動態網頁-新手爬蟲也可以很輕鬆-468a5533828a
# https://www.learncodewithmike.com/2020/05/python-selenium-scraper.html
# https://ithelp.ithome.com.tw/articles/10204231
# https://freelancerlife.info/zh/blog/python%E7%B6%B2%E8%B7%AF%E7%88%AC%E8%9F%B2%E6%95%99%E5%AD%B8-selenium%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9C/
# https://freelancerlife.info/zh/blog/python-web-scraping-overview/
# https://www.newscan.com.tw/all-faq/faq-detail-15.htm
# http://www.j4.com.tw/customers-works/常聽到靜態網頁，動態網頁，如何分別？/


#%%


                      # ]) # 做法0：不儲存Photo資料

                     # ]) # 做法0：不儲存Photo資料


        #               str(photo_list[0])]) # 做法2
        # if len(photo_list) > 1: # 做法2
        #     for w in photo_list[1:]: # 做法2
        #         sheet.append(["","","","","",str(w)]) # 做法2
