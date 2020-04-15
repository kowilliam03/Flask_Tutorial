# ```Flask``` Tutorial

## 目錄
- ### [1. 什麼是後端(Back-End)?](#1.-什麼是後端(Back-End?) )
- ### [2. ```Flask```簡介與安裝](#2.-```Flask```簡介與安裝)
- ### [3. 開發工具介紹](#3.-開發工具介紹)
- ### [4. Virtualenv 介紹](#4.-Virtualenv 介紹)
- ### [5. Flask 介紹](#5.-Flask 介紹)


### 1. 什麼是後端(Back-End)?
> #### 網頁後端通常指的是運行在網站伺服器上的程式，負責處理網站的運行邏輯、業務邏輯。

常跟後端一同提起的是前端，前端主要包含：靜態的網頁(HTML、CSS)、網頁上的特效(JavaScript)...等。前端與後端互相配合，當使用者要求查看資料時，前端會向後端發起請求，後端會根據工程師定義好的邏輯，將資料從資料庫中取出，並按照指定的格式回傳給前端，前端在將資料展現給使用者看。

用麥當勞來比喻前後端的關係：前端就像是在前檯負責幫客戶點餐，不需要知道每份餐點怎麼做出來的，只需要將客戶的要求轉換成指定的格式，透過POS機傳給後端。後端就像廚房，不需要了解客戶說了什麼，只需要根據POS機的指示將餐點完成後，將餐點放到指定的位置，最後再由前檯人員將餐點包裝好後交給客戶(網頁前端將後端回傳的資料處理後，展現給用戶看)。


### 2. ```Flask```簡介與安裝
> [```Flask```](https://flask.palletsprojects.com/en/master/)是一個使用Python編寫的輕量級Web應用框架。基於Werkzeug WSGI工具箱和Jinja2 模板引擎。```Flask```使用BSD授權。  
> ```Flask```被稱為「microframework」，因為它使用簡單的核心，用extension增加其他功能。```Flask```沒有預設使用的資料庫、表單驗證工具。然而，```Flask```保留了擴增的彈性，可以用```Flask```-extension加入這些功能：ORM、表單驗證工具、檔案上傳、各種開放式身分驗證技術。  -- 維基百科

安裝方式：
```bash
pip install flask
```

### 3. 開發工具介紹
開發```Flask```或是其他Python程式，可以使用各種 Editor 或 IDE ，這裡我們主要使用的是微軟提供的開源 Editor：[Visual Studio Code](https://code.visualstudio.com/)(簡稱：VSCode或VSC)，可以到[這裡](https://code.visualstudio.com/)安裝。也可以使用自己習慣的開發工具。  
安裝好VSCode後，為了讓VSCode更方便開發Python程式，首先要做的是安裝插件：

 1. 點擊左手邊Extensions的Icon或是用快捷鍵 Ctrl + Shift + X 開啟 Extensions 安裝界面。
 2. 搜尋 Python
 3. 找到第一個由微軟提供的 Python Extension 並點擊安裝。
 4. 安裝完成後，根據提示，重新啟動 VSCode。
 5. 接著使用 VSCode 開啟app.py ，開始寫```Flask```！！

### 4. Virtualenv介紹
再開始寫```Flask```之前，先介紹Virtaulenv。
> [```virtualenv```](https://virtualenv.pypa.io/en/latest/) is a tool to create isolated Python environments.

之所以要使用```Virtualenv```，是因為Python有許多不同的版本(如：3.5、3.6...等等)，Python 有許多第三方套件，這些套件也不斷的會推出新的版本，而這些第三方套件本身也可能會使用到其他的第三方套件，而且使用的版本不見得會是最新的，因此常會有版本不相容的問題發生。而```Virtualenv```就是為了解決這種問題。

我們利用```Virtualenv```為專案創建一個獨立的Python環境，這樣每個專案都有自己獨立的 Python 環境，在各自的環境中安裝專案所需的套件，彼此就不會互相影響了。

安裝方式：
```bash
pip install virtualenv
```

常用指令
```bash
python -m venv demo  # 創建名為demo的虛擬環境

# 啟用虛擬環境
# Windows
demo\Scripts\activate.bat

# Unix、MacOS
source demo/bin/activate
```
> [查看更多](https://docs.python.org/zh-tw/3/tutorial/venv.html)

虛擬環境創建及啟用成功後，在 VSCode 中新開啟一個 Terminal ，看看有什麼變化吧~~

接著便在新建立好的環境中，安裝 Flask 吧！！

### 5. Flask 介紹
[參考網址](https://flask.palletsprojects.com/en/master/quickstart/)