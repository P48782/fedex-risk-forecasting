<p align="center">
  <img src="fedex_logo.png" alt="FedEx Logo" width="200"/>
</p>

# 📦 FedEx Risk Forecasting and Analytics

This project analyzes FedEx shipment risk by applying data cleaning, forecasting, risk scoring, and prescriptive analytics using Python and Power BI.

---

## 📁 Dataset Access

### 🔹 Cleaned Input Dataset
The base dataset used in this project is hosted on Kaggle.

👉 [Request Access to Dataset on Kaggle](https://kaggle.com/datasets/d6eb37a650632f3a572239824ed20d48f3d9999008231d21938b826e8bfe5134)

**File included:**
- `fedex_delivery_data.csv` – Cleaned dataset used for all modeling and forecasting

---

### 🔹 Forecasting & Modeling Outputs (Google Drive)

Due to GitHub file size limits, the forecasting and prescriptive modeling outputs are hosted on Google Drive:

👉 [Download Modeling Outputs (Google Drive)](https://drive.google.com/drive/folders/1GWo2l1rqBqftsqmtreYNLu0o8dW1EzZf?usp=share_link)

**Files included:**
- `weekly_forecast.csv` – Forecasted weekly delivery risk
- `route_risk_scores.csv` – Risk scores per route
- `prescriptive_actions.csv` – Model-suggested actions per route
- `fedex_cleaned.csv` – Used in modeling (subset of base)
- `fedex_dashboard.pbix` – Power BI dashboard file (can be downloaded and opened locally)

> 📂 Place these files inside a `/data/` folder when running code or opening the dashboard locally.

---

## 📊 FedEx Shipment Dashboard – Interactive Preview

🚧 The interactive version of this dashboard is hosted on my university’s Power BI workspace.  
🔐 Access may be restricted to university users only. If you’re unable to view it, please refer to the PDF snapshot below.

🔗 **Interactive Dashboard (hosted at university)**:  
[View Dashboard in Power BI Service](https://app.powerbi.com/groups/me/reports/9a381687-6805-473b-aa31-071a2d5e0d8b/8314f80ec30e41520942?experience=power-bi)

📄 **PDF Snapshot of Dashboard**:  
[Download Dashboard PDF](https://github.com/P48782/fedex-risk-forecasting/blob/main/Fedex%20forecasting.pdf)

---

## 📈 Forecasting & Risk Analysis

This project includes a comprehensive time series forecasting module and route-level risk analysis to support smarter delivery execution.

### 🔮 Forecasting Highlights

- **SARIMA time series model** was used to forecast weekly shipment volumes over a 12-week horizon.
- Weekly shipment cycles and seasonal surges (especially around Q2–Q3) were identified.
- Forecasted volumes ranged from **~1,000 to 1,200 shipments/week**, with **clear mid-quarter peaks**, enabling proactive staffing and fleet scaling.
- Forecasts were exported to Power BI for visualization.

📄 Forecast output: [`weekly_forecast.csv`](https://drive.google.com/drive/folders/1GWo2l1rqBqftsqmtreYNLu0o8dW1EzZf?usp=share_link)

### ⚠️ Risk Modeling Insights

- Shipment delays were mapped across all FedEx routes.
- **Top delay-prone routes** (e.g., ONT → SAN, HPN → PIA, SDF → SPI) were identified based on historical trends.
- A custom delay risk score was calculated per route using average delay, variance, and failure rate.
- **Prescriptive recommendations** were generated suggesting:
  - Buffer time allocations (e.g., 45–60 minutes)
  - Route rerouting or priority reshuffling

📄 Risk & prescription outputs: [`route_risk_scores.csv`](https://drive.google.com/drive/folders/1GWo2l1rqBqftsqmtreYNLu0o8dW1EzZf?usp=share_link)

---

## 🧪 How to Reproduce

1. Clone this GitHub repo:
   ```bash
   git clone https://github.com/yourusername/fedex-risk-forecasting.git
