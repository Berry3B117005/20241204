import tkinter as tk

# 建立主視窗
root = tk.Tk()
root.title("聯絡資訊爬蟲")

# 外層空白欄位（Frame），背景設置為透明（與視窗背景一致）
外層欄位 = tk.Frame(root, width=300, height=200)  # 不指定背景色，保持透明效果
外層欄位.pack_propagate(False)  # 防止自動縮放
外層欄位.pack(padx=20, pady=20)
# 函數：檢查網址格式是否有效
def is_valid_url(url):
    regex = r'^(https?://)?([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,6}(/[\w-]*)*$' #正規表示式
    return re.match(regex, url) is not None

# 函數：提交網址並檢查其有效性
def submit_url():
    url = url_entry.get()  # 取得用戶輸入的網址
    if is_valid_url(url):
        result_label.config(text="有效的網址: " + url, fg="green")
    else:
        result_label.config(text="無效的網址", fg="red")

# 創建標籤，說明輸入網址
url_label = tk.Label(root, text="請輸入網址：")
url_label.pack(pady=5)

# 創建網址輸入框
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# 創建提交按鈕，檢查網址是否有效
submit_button = tk.Button(root, text="抓取", command=submit_url)
submit_button.pack(pady=10)

# 顯示結果的標籤
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()