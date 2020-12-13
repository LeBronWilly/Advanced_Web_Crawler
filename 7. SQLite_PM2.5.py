# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14

@author: Willy Fang
# 講解方法

Python3有內建一個嵌入式的資料庫（DB）：SQLite，它使用一個文件儲存整個DB，操作方便，可以在Python使用SQL指令管理DB，完成資料表（DT）的增刪改查（CRUD）
"""
#%%

import sqlite3, requests, os
import json
# from selenium import webdriver


current_path = os.path.dirname(__file__) # 取得目前路徑，儲存DB用
conn = sqlite3.connect(current_path+'/'+'MyDB.sqlite') # 必須建立和DB的連線
cursor = conn.cursor() # 建立cursor物件，搭配execute方法可以完成DT的增刪改查

# 使用SQL新增/建立一個DT
sqlstr='''
CREATE TABLE IF NOT EXISTS TablePM25 ("Num." INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE ,"SiteName" TEXT NOT NULL ,"PM2.5" INTEGER ,"AQI(空氣品質指標)" INTEGER ,"Status" TEXT)
''' # 宣告SQL指令（You can only execute one statement at a time）
cursor.execute(sqlstr) # 執行SQL指令，可以完成DT的增刪改查

#%%

# 資料：https://opendata.epa.gov.tw/Data/Contents/AQI/
url = "https://opendata.epa.gov.tw/api/v1/AQI?%24skip=0&%24top=1000&%24format=json" # OPEN API之json
html = requests.get(url).text # 讀取網頁原始碼
jsondata = json.loads(html) # 將網頁內容轉換為list(裡面的元素是dict)


print("Open Data's PublishTime: "+ jsondata[0]["PublishTime"])
print('\nUpdating The Database......\n') # 提示用
cursor.execute("DELETE FROM TablePM25") # 刪除DT中的所有內容，並非刪除DT
conn.commit() # 執行DB更新（這個才真正會run以上的cursor.execute）


#%%

# n=1 # 可用來填Num.的欄位

for site in jsondata:
    # 處理資料
    SiteName=site["SiteName"]


    try:
        AQI=int(site["AQI"])
    except:
        AQI=-1

    if site["PM2.5"] == "ND":
        continue
    elif site["PM2.5"] == "":
        PM25=-1
    else:
        PM25=int(site["PM2.5"])

    if site["Status"] == "":
        Status="(Null)"
    else:
        Status=site["Status"]


    print("SiteName:{}   PM2.5={}".format(SiteName,PM25)) # 提示用
    sqlstr="insert into TablePM25 values(null,'{}',{},{},'{}')" .format(SiteName,PM25,AQI,Status) # 新增一筆記錄
    cursor.execute(sqlstr) # 執行上面的SQL指令
    conn.commit() # 執行DB的更新（這個才真正會run以上的cursor.execute）

    # n+=1

print('\nPublishTime: ' + site["PublishTime"])
print('Updated The Database Successfully!')
conn.close() # 關閉DB連線