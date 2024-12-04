import requests
import re
import sqlite3
import tkinter as tk
conn = sqlite3.connect('school.db')  # 連線資料庫
cursor = conn.cursor()  # 建立 cursor 物
# 發送 GET 請求
# httpbin.org 網站可讓我們測試 http 的各種方法
# http://httpbin.org/get 會回應伺服器收到的 GET 請求內容
response = requests.get('https://csie.ncut.edu.tw/content.php?key=86OP82WJQO')

# 檢查請求是否成功
# 方法1：使用 response.status_code
if response.status_code == 200:
    print("Request 成功")
else:
    # 若請求失敗，顯示錯誤碼
    print(f'請求失敗，錯誤碼為: {response.status_code}')
    exit(1)  # 使用 exit(1) 表示異常結束並返回錯誤碼
# 顯示回應的物件屬性
print(f'網址：{response.url}')          # 網址
print(f'網頁編碼：{response.encoding}')  # 網頁編碼
response.encoding = 'utf-8' if response.encoding != 'utf-8' else response.encoding

print('標頭資訊', response.headers)      # 回應的標頭資訊
print(response.headers['content-type'])  # 顯示網頁回應的內容類型

print('cookies 資訊')
cookies = response.cookies              # cookies 資訊
for key, value in cookies.items():
    print(f"{key}: {value}")
print('網頁內容')
print(response.text)                    # 網頁內容
print()

# 描述 Email 的正規表示式物件 pattern
pattern = re.compile(r'\b[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b')
# pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
# pattern = re.compile(r'mailto://([^"]+)')

URL = "https://csie.ncut.edu.tw/content.php?key=86OP82WJQO"
response = requests.get(URL)
match_list = pattern.findall(response.text)  # 從網頁原始碼中尋找所有 Email
unique_emails = list(set(match_list))  # 將列表轉換為集合再轉回列表，以去除重複的 Email
for email in unique_emails:
    print(email)

# 描述姓名的正規表示式物件 pattern
pattern = re.compile(r'<div class="member_name"><a href="[^"]+">([^<]+)</a>')
match_list = pattern.findall(response.text) # 從網頁原始碼中尋找所有姓名
for _ in match_list:
    print(_)
    
title_pattern = re.compile(r'<div class="member_info_content">([^<]+)</div>')

# 使用正規表示式提取所有職稱
title_pattern = re.compile(r'<div class="member_info_content">([^<]+)</div>')
title_match_list = title_pattern.findall(response.text)

if not title_match_list:
    print("未找到職稱")
else:
    print("職稱:")
    for title in title_match_list:
        print(title)


form = tk.Tk()  # 呼叫 tk.TK() 建立視窗
form.title("聯絡資訊爬蟲")

form.geometry("640x480")  # 設定視窗寬高



form.mainloop()  # 等待處理事件保持視窗執行