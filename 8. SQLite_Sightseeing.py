# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16

@author: Willy Fang

Python3有內建一個嵌入式的資料庫（DB）：SQLite，它使用一個文件儲存整個DB，操作方便，可以使用SQL指令管理DB，完成資料表（DT）的增刪改查
"""
#%%

import sqlite3, requests, os
import json

current_path = os.path.dirname(__file__)
conn = sqlite3.connect(current_path+'/'+'MyDB.sqlite')
cursor = conn.cursor()

sqlstr='''
CREATE TABLE IF NOT EXISTS TableSightSeeing ("Num." INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE ,"Name" TEXT NOT NULL ,"Address" TEXT ,"Longitude " float ,"Latitude " float ,"Desc." TEXT)
''' # 宣告SQL指令，這個是新的DT！
cursor.execute(sqlstr)

#%%

# 資料：https://data.gov.tw/dataset/7777
url = "https://gis.taiwan.net.tw/XMLReleaseALL_public/scenic_spot_C_f.json"
html = requests.get(url).text.encode('utf-8')
pre_jsondata = json.loads(html)


print("Open Data's Updatetime: "+ pre_jsondata["XML_Head"]["Updatetime"])
print('\nUpdating The Database......')
jsondata = pre_jsondata["XML_Head"]["Infos"]["Info"]
cursor.execute("DELETE FROM TableSightSeeing")
conn.commit()

#%%

n=1
for site in jsondata[:10]:
    Name=site["Name"]
    Address=site["Add"]
    Longitude=site["Px"]
    Latitude=site["Py"]
    Desc=str(site["Toldescribe"])
    print("Name:{}".format(Name))
    
    try:
        sqlstr='insert into TableSightSeeing values({},"{}","{}",{},{},"{}")' .format(n,Name,Address,Longitude,Latitude,Desc) # 換個方式寫
        cursor.execute(sqlstr)
    except: # 還是會有部分資料有問題......
        Desc=str(site["Toldescribe"]).replace("'", "’")
        sqlstr="insert into TableSightSeeing values({},'{}','{}',{},{},'{}')" .format(n,Name,Address,Longitude,Latitude,Desc) # 換個方式寫
        cursor.execute(sqlstr)

    conn.commit()
    n+=1

print('Updated The Database!')
conn.close()


#%%

'🙏內推/工作機會邀約懇請私訊小盒子或領英👻'