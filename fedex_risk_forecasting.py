# FedEx Shipment Risk Forecasting and Planning Project

# 📁 Repo Structure
# -----------------
# fedex-risk-forecasting/
# ├── data/
# │   ├── raw/                  # Original downloaded data (fedexdata.csv)
# │   └── processed/            # Cleaned and transformed data
# ├── notebooks/
# │   ├── 01_eda_and_cleaning.ipynb   # Initial exploration and preprocessing
# │   ├── 02_forecasting.ipynb          # Time series forecast of shipment demand
# │   ├── 03_risk_analysis.ipynb        # Delay prediction and execution variation
# │   └── 04_prescriptive_modeling.ipynb # Optimization of routing/capacity
# ├── src/
# │   ├── data_utils.py             # Helper functions for data loading/cleaning
# │   ├── forecast_model.py         # Reusable time series model code
# │   └── optimizer.py              # Code for risk-aware prescriptive planning
# ├── reports/
# │   └── executive_summary.md     # Markdown summary of key insights
# ├── visuals/                # Saved plots and charts
# ├── requirements.txt         # Python dependencies
# └── README.md                # Project overview and setup instructions

# Let's now start with the EDA notebook template:

# notebooks/01_eda_and_cleaning.ipynb (outline below)

"""
# 01 - Exploratory Data Analysis & Cleaning

## 📦 Dataset: FedEx Shipment Records

### 1. Import Packages
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
```

### 2. Load Data
```python
df = pd.read_csv('../data/raw/fedexdata.csv')
df.head()
```

### 3. Initial Overview
```python
print(df.info())
print(df.describe())
print(df.columns)
df.isnull().sum()
```

### 4. Feature Engineering
- Convert dates to datetime format
- Create delay columns (actual - planned)
- Derive weekday/weekend/holiday indicators

```python
df['Pickup_Date'] = pd.to_datetime(df['Pickup_Date'])
df['Delivery_Date'] = pd.to_datetime(df['Delivery_Date'])
df['Delay'] = (df['Delivery_Date'] - df['Planned_Delivery']).dt.days
```

### 5. Univariate Analysis
```python
sns.histplot(df['Delay'], kde=True)
plt.title('Distribution of Delivery Delays')
```

### 6. Bivariate: Delay by Region, Day of Week, Carrier
```python
sns.boxplot(x='Carrier', y='Delay', data=df)
plt.xticks(rotation=45)
```

### 7. Save Cleaned Version
```python
df.to_csv('../data/processed/fedex_cleaned.csv', index=False)
```

"""
# Next: Forecasting weekly volume or delays by hub/region
# (covered in 02_forecasting.ipynb)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Set plotting style
sns.set(style="whitegrid")
# Load the raw dataset
df = pd.read_csv('data/raw/fedex_delivery_data.csv')

# Preview the data
df.head()

# Dataset summary
print(df.info())
print(df.describe())
print("Columns:", df.columns.tolist())

# Check for missing values
print("Missing values:\n", df.isnull().sum())

print(df.columns.tolist())

# 1. Rename to standard expected column names if needed
df.rename(columns=lambda x: x.strip(), inplace=True)  # remove extra spaces
df.rename(columns={'DayOfMonth': 'DayofMonth'}, inplace=True)  # in case it's mis-capitalized

# 2. Now create Pickup Date safely
df['Pickup_Date'] = pd.to_datetime(dict(
    year=df['Year'],
    month=df['Month'],
    day=df['DayofMonth']
))

# 3. Create Delivery Date using Shipment_Delay
df['Delivery_Date'] = df['Pickup_Date'] + pd.to_timedelta(df['Shipment_Delay'], unit='D')

# 4. Calculate Delay (if needed, otherwise skip)
df['Delay'] = df['Shipment_Delay']

# 5. Weekday and Weekend flag
df['Pickup_DayOfWeek'] = df['Pickup_Date'].dt.dayofweek
df['Is_Weekend'] = df['Pickup_DayOfWeek'].isin([5, 6])

# Preview
print(df[['Pickup_Date', 'Delivery_Date', 'Delay', 'Pickup_DayOfWeek', 'Is_Weekend']].head())

# Histogram of delivery delays
plt.figure(figsize=(8, 5))
sns.histplot(df['Delay'], kde=True, bins=30)
plt.title('Distribution of Delivery Delays')
plt.xlabel('Delay (Days)')
plt.ylabel('Frequency')
plt.show()

# Average Delay by Carrier (Aggregated)
carrier_avg = df.groupby('Carrier_Name')['Delay'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='Carrier_Name', y='Delay', data=carrier_avg)
plt.title('Average Delivery Delay by Carrier')
plt.xticks(rotation=45)
plt.ylabel('Average Delay (Days)')
plt.show()

# Delay by Day of Week
df['Pickup_Weekday'] = df['Pickup_Date'].dt.day_name()
plt.figure(figsize=(10, 6))
sns.boxplot(x='Pickup_Weekday', y='Delay', data=df, order=[
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
plt.title('Delivery Delays by Pickup Day')
plt.xticks(rotation=45)
plt.show()

# Save the cleaned and enriched dataset
import os

# Ensure the directory exists
os.makedirs('data/processed', exist_ok=True)

# Then save the cleaned CSV into that folder
df.to_csv('data/processed/fedex_cleaned.csv', index=False)

