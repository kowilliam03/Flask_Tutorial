# Flask Tutorial

## 目錄
- ### [1. 什麼是後端(Back-End)?](#1.-什麼是後端(Back-End?) )
- ### [2. Flask簡介與安裝](#2.-Flask簡介與安裝)
- ### [3. 開發工具介紹](#3.-開發工具介紹)
- ### 3. Flask基本語法介紹


### 1. 什麼是後端(Back-End)?
> #### 網頁後端通常指的是運行在網站伺服器上的程式，負責處理網站的運行邏輯、業務邏輯。

常跟後端一同提起的是前端，前端主要包含：靜態的網頁(HTML、CSS)、網頁上的特效(JavaScript)...等。前端與後端互相配合，當使用者要求查看資料時，前端會向後端發起請求，後端會根據工程師定義好的邏輯，將資料從資料庫中取出，並按照指定的格式回傳給前端，前端在將資料展現給使用者看。

### 2. Flask簡介與安裝
> Flask是一個使用Python編寫的輕量級Web應用框架。基於Werkzeug WSGI工具箱和Jinja2 模板引擎。Flask使用BSD授權。  
>Flask被稱為「microframework」，因為它使用簡單的核心，用extension增加其他功能。Flask沒有預設使用的資料庫、表單驗證工具。然而，Flask保留了擴增的彈性，可以用Flask-extension加入這些功能：ORM、表單驗證工具、檔案上傳、各種開放式身分驗證技術。  -- 維基百科

安裝方式：
```bash
pip install flask
```

### 3. 開發工具介紹
開發Flask或是其他Python程式，可以使用各種Editor或IDE，這裡我們主要使用的是微軟提供的開源Editor：[Visual Studio Code](https://code.visualstudio.com/)(簡稱：VSCode或VSC)，可以到[這裡](https://code.visualstudio.com/)安裝。也可以使用自己習慣的開發工具。  
安裝好VSCode後，為了讓VSCode更方便開發Python程式，首先要做的是安裝插件：

 1. 點擊左手邊Extensions的Icon或是用快捷鍵Ctrl + Shift + X開啟Extensions安裝界面。
 2. 搜尋Python
 3. 找到第一個由微軟提供的Python Extension並點擊安裝。
 4. 安裝完成後，根據提示，重新啟動VSCode。
 5. 接著就可以使用VSCode開始寫Flask了。