# 台灣鐵路資料應用學習筆記 / Taiwan Railway Data Application Learning Notes

This repository is a collection of learning notes and code examples for utilizing the Ministry of Transportation and Communications’ **Transport Data eXchange (TDX)** platform to access Taiwan railway-related data. It is designed to help developers understand how TDX services work, how to apply for and use its APIs, and provides practical Python code for querying train data.

---

## 📚 專案目標 / Project Goals

This project documents the author's learning and hands-on experience with TDX railway APIs, including:

- **TDX Service Overview**: Understanding available services, pricing models, and membership tiers.
- **API Usage Tutorial**: Step-by-step instructions for accessing Taiwan railway data using TDX APIs.
- **Code Examples**: Python code to demonstrate API requests and data handling.

---

## ✨ TDX 運輸資料流通服務簡介 / Introduction to TDX

TDX is a data platform offered by Taiwan's Ministry of Transportation. It integrates and opens various transportation-related datasets, including:

- Railway
- Highway
- Aviation
- Shipping
- Tourism
- Meteorology
- Bicycles
- Mapping data

---

## 🧾 會員與計費 / Membership and Pricing

| 會員等級 | 限制與權益 |
|---------|------------|
| **訪客 (Visitor)** | Daily limit: 20 API calls; IP binding required. |
| **一般會員 (General Member)** | 3 free virtual points/month; max 5 calls/min per API key. |
| **銅 / 銀 / 金 / 白金會員** | Paid tiers with higher usage limits. |
| **專案會員 (Project Member)** | Custom pricing for >20,000 virtual points/month. |

---

## 📝 申請流程 / Application Procedure

To access TDX APIs:

1. Register at [TDX 官網](https://tdx.transportdata.tw/)
2. Complete mobile and email verification.
3. Apply for API access and wait for approval.
4. Start using your API key.

---

## 🚀 如何使用本專案 / How to Use This Project

This project includes Jupyter Notebooks with hands-on examples.

### ✅ 前置需求 / Prerequisites

- Python 3.x
- Jupyter Notebook
- A valid TDX API account and key

### 🛠️ 操作步驟 / Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/1daniel3333/TW_railway.git
   cd TW_railway
   ```

2. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

3. Open `.ipynb` files to explore the code and learning notes.

---

## 💡 學習資源 / Learning Resources

### 官方與參考資源

- [TDX 是什麼？如何計費與使用？ (Medium)](https://medium.com/)
- [TDX API 使用教學 (Medium)](https://medium.com/)
- [TDX API 文件 (GitBook)](https://tdx.gitbook.io/)
- [TDX 官方 GitHub 範例](https://github.com/)
- [TDX Swagger API 線上測試工具](https://tdx.transportdata.tw/)
- [台灣鐵路局 - 車站代碼表](https://tip.railway.gov.tw/tra-tip-web/tip/tip00C/tipC21/viewStaCode)

---

## 🤝 貢獻方式 / Contributing

Contributions are welcome! You can:

- Improve code examples
- Add new TDX API use cases
- Fix bugs or improve documentation

### GitHub 貢獻流程

1. Fork this repo
2. Create a new branch
3. Make your changes
4. Submit a Pull Request

---

## 📄 授權 / License

This project is licensed under the [MIT License](LICENSE).
