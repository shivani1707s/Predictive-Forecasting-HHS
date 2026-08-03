
# 📊 Predictive Forecasting of Care Load & Placement Demand

A machine learning and time-series forecasting project that predicts future care load and placement demand for the **U.S. Department of Health and Human Services (HHS) – Unaccompanied Alien Children (UAC) Program**.

The project transforms historical operational data into predictive intelligence, enabling proactive planning for shelter capacity, healthcare staffing, and child welfare services.

---

## 📌 Project Overview

The UAC Program operates in a highly dynamic environment where border activity, policy changes, and humanitarian events can rapidly increase the number of children entering federal care.

This project aims to forecast:

- 👶 Future number of children in HHS care
- 📈 Future discharge (placement) demand
- ⚠️ Capacity stress and imbalance between incoming transfers and exits
- 📅 Short-term forecasts (7, 14, and 30 days)

The solution combines **Time Series Forecasting** and **Machine Learning** models to support data-driven decision making.

---

## 🎯 Objectives

### Primary Objectives

- Forecast children in HHS care
- Predict discharge demand
- Estimate future care load
- Forecast intake vs discharge imbalance

### Secondary Objectives

- Provide early warning indicators
- Compare forecasting models
- Quantify forecast uncertainty
- Support proactive healthcare planning

---

## 📂 Dataset

The dataset contains daily operational statistics including:

| Column                                         | Description              |
| ---------------------------------------------- | ------------------------ |
| Date                                           | Reporting Date           |
| Children apprehended and placed in CBP custody | Daily intake volume      |
| Children in CBP custody                        | Current CBP care load    |
| Children transferred out of CBP custody        | Flow into HHS care       |
| Children in HHS Care                           | Current HHS care load    |
| Children discharged from HHS Care              | Daily sponsor placements |

---

## 🔍 Project Workflow

```
Data Collection
        │
        ▼
Data Cleaning
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Feature Engineering
        │
        ▼
Time Series Forecasting
        │
        ▼
Machine Learning Models
        │
        ▼
Model Evaluation
        │
        ▼
Future Forecasts
        │
        ▼
Interactive Streamlit Dashboard
```

---

## ⚙️ Feature Engineering

Features used for forecasting include:

- Lag Features (1, 7, 14 days)
- Rolling Mean
- Rolling Standard Deviation
- Net Pressure Indicator
- Day of Week
- Month
- Quarter
- Weekend Indicator
- Calendar Effects

---

## 🤖 Forecasting Models

### Baseline Models

- Naïve Forecast
- Moving Average

### Statistical Models

- ARIMA
- SARIMA
- Exponential Smoothing

### Machine Learning Models

- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost Regressor
- LightGBM Regressor

---

## 📊 Evaluation Metrics

Models are evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- Mean Absolute Percentage Error (MAPE)
- Forecast Accuracy (%)
- Forecast Stability
- Capacity Breach Probability

---

## 📈 Dashboard Features

The Streamlit dashboard provides:

- Historical Care Load Trends
- Future Care Load Forecast
- Discharge Demand Forecast
- Model Comparison
- Forecast Confidence Intervals
- Capacity Stress Indicators
- Interactive Forecast Horizon Selection
- KPI Cards
- Scenario Comparison

---

## 🛠️ Tech Stack

### Programming Language

- Python 3.11

### Libraries

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Scikit-learn
- Statsmodels
- XGBoost
- LightGBM
- Prophet
- Streamlit
- Joblib

---

## 📁 Project Structure

```
Predictive-Forecasting-HHS/

│── data/
│── notebooks/
│── src/
│── models/
│── outputs/
│── reports/
│── assets/

│── streamlit_app.py
│── requirements.txt
│── README.md
│── .gitignore
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/shivani1707s/Predictive-Forecasting-HHS.git
```

Move into the project folder

```bash
cd Predictive-Forecasting-HHS
```

Create virtual environment

```bash
python -m venv .prevenv
```

Activate virtual environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Streamlit Dashboard

```bash
streamlit run streamlit_app.py
```

---

## 📊 Expected Outputs

- Time Series Analysis
- Feature Engineered Dataset
- Future Care Load Forecasts
- Discharge Demand Forecasts
- Model Performance Comparison
- Forecast Confidence Intervals
- Interactive Dashboard

---

## 💡 Future Enhancements

- Deep Learning (LSTM/GRU)
- Facebook Prophet Optimization
- Real-time Data Integration
- Automated Model Retraining
- Cloud Deployment
- Explainable AI (SHAP)

---

## 📜 License

This project is intended for educational and research purposes.

---

## 👩‍💻 Author

**Shivani**

GitHub: https://github.com/shivani1707s

---

⭐ If you found this project useful, consider giving it a star!
