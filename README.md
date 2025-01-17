# sa-law-db
A law database for student association, which written in React and Flask + SQLAlchemy.

## 專案簡介
學生會法規資料庫系統旨在為學生提供便捷的法規查詢平台，提升資訊透明度及學生對校園法規的了解。該系統包含法規管理、搜尋功能，以及版本修訂記錄功能，並為管理員提供專門的後台操作介面。

## 功能特色
- 法規查詢與顯示：
  - 支援按章節、條文檢視。
  - 可查看歷史修訂記錄。
- 搜尋功能：
  - 按法規名稱或條文關鍵字搜索。
- 管理員後台：
  - 新增、修改法規內容。
  - 處理條文包含複雜結構（如「之一」、「之二」）。
  - 記錄修訂歷史。

## 技術架構
- **後端**：Flask + SQLAlchemy
- **前端**：React
- **資料庫**：MariaDB
- **系統需求**：
  - 作業系統：Linux/Windows/MacOS
  - Python 版本：3.9 以上
  - Node.js 版本：16 以上

## 安裝與執行
### 環境準備
1. 確認安裝 Python 與 Node.js。
2. 安裝 MariaDB 並啟動。

### 安裝步驟
```bash
# 克隆專案
git clone https://github.com/your-repo/student-law-database.git
cd student-law-database

# 安裝後端依賴
cd backend
pip install -r requirements.txt

# 安裝前端依賴
cd ../frontend
npm install
```

### 啟動專案
```bash
# 啟動後端
cd backend
python app.py

# 啟動前端
cd ../frontend
npm start
```

## 使用說明
1. 前往 http://localhost:3000 瀏覽前端介面。
2. 使用搜尋框輸入法規名稱或條文關鍵字進行查詢。
3. 若有管理員權限，登入後可進入後台進行法規管理。

## 測試
```bash
# 後端測試
cd backend\pytest

# 前端測試
cd frontend
npm test
```

## 部署說明
1. 配置伺服器環境，建議使用 Nginx 與 Gunicorn 部署後端。
2. 前端可打包為靜態文件，並透過 Nginx 提供服務。
3. 配置資料庫連線，確保 MariaDB 正常運行。

## 貢獻指南
1. Fork 此專案，並建立新的分支。
2. 提交修改並發送 Pull Request。
3. 確保代碼通過所有測試。

## 版權與授權
此專案採用 MIT 授權，詳見 [LICENSE](./LICENSE)。

## 聯絡方式
- 專案維護者：蘇柏郡（Kazan）
- Email: me@kazan.tw
- GitHub: [kazanTW](https://github.com/kazanTW)