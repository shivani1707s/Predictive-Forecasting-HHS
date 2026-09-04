# 📊 Predictive Forecasting of Care Load & Placement Demand

A machine learning and time-series forecasting project for predicting future care load and placement demand in the **U.S. Department of Health and Human Services (HHS) – Unaccompanied Alien Children (UAC) Program**.

The project transforms historical operational data into predictive insights that can support proactive planning for care capacity, staffing, placement operations, and resource allocation.

---

## 📌 Project Overview

The HHS UAC Program operates in a dynamic environment where changes in intake, transfers, and discharges can affect the number of children requiring care.

This project focuses on forecasting:

- 👶 Future number of children in HHS care
- 📈 Short-term and medium-term care-load demand
- 🔄 Operational pressure from transfers and discharges
- ⚠️ Potential capacity-risk periods
- 📅 1-day, 7-day, 14-day, and 30-day forecasts
- 📊 Forecast uncertainty using empirical prediction intervals

The project combines statistical forecasting approaches with machine learning, with **Gradient Boosting** providing the primary multi-horizon forecasting model.

---

# 🎯 Objectives

## Primary Objectives

- Forecast the number of children in HHS care.
- Predict future care-load demand.
- Identify changes in operational pressure.
- Produce forecasts across multiple planning horizons.
- Provide uncertainty estimates around forecasts.

## Secondary Objectives

- Compare machine learning and baseline forecasting approaches.
- Identify potential capacity-risk periods.
- Evaluate forecast errors across different horizons.
- Provide an interactive dashboard for operational exploration.

---

# 📂 Dataset

The dataset contains operational statistics reported over time.

| Column                                              | Description                           |
| --------------------------------------------------- | ------------------------------------- |
| `Date`                                            | Reporting date                        |
| `Children apprehended and placed in CBP custody*` | Children entering CBP custody         |
| `Children in CBP custody`                         | Children currently in CBP custody     |
| `Children transferred out of CBP custody`         | Children transferred from CBP custody |
| `Children in HHS Care`                            | Children currently in HHS care        |
| `Children discharged from HHS Care`               | Children discharged from HHS care     |

The cleaned dataset contains **720 reported observations** covering:

**January 12, 2023 – December 21, 2025**

The source data contains reporting gaps, including systematic gaps on certain weekdays. These gaps were considered during preprocessing and model development.

---

# 🔍 Project Workflow

```text
Raw Operational Data
        │
        ▼
Data Cleaning
        │
        ▼
Missing-Date Analysis
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Feature Engineering
        │
        ▼
Baseline & Statistical Models
        │
        ▼
Machine Learning Forecasting
        │
        ▼
Multi-Horizon Evaluation
        │
        ▼
Uncertainty Estimation
        │
        ▼
Capacity-Risk Analysis
        │
        ▼
Interactive Streamlit Dashboard
```

# 🧹 Data Preparation

The preprocessing stage included:

* Removing completely empty records.
* Converting dates into datetime format.
* Converting operational measures into numeric values.
* Examining missing reporting dates.
* Investigating weekday reporting patterns.
* Creating calendar-based variables.
* Creating lagged operational features.
* Creating rolling statistics.
* Constructing operational pressure indicators.

A key finding from the data-quality analysis was that missing reporting dates were  **not completely random** . Friday and Saturday observations were substantially underrepresented in the source data.

This is an important limitation when interpreting calendar-based forecasting results.

# ⚙️ Feature Engineering

The forecasting dataset includes features representing temporal patterns and operational conditions.

### Calendar Features

* Day of week
* Day of month
* Month
* Quarter
* Year
* Week of year
* Weekend indicator

### Lag Features

* Previous HHS care load
* 7-period lag
* 14-period lag
* 28-period lag
* Transfer lags
* Discharge lags

Rolling Features

* 7-period rolling mean
* 14-period rolling mean
* 7-period rolling standard deviation
* 14-period rolling standard deviation

### Operational Features

* Net pressure
* Discharge-to-transfer ratio

These features allow the model to capture recent trends, operational momentum, variability, and calendar effects.

# 🤖 Forecasting Models

## Baseline Models

The project evaluated simple forecasting approaches including:

* Naïve forecasting
* 7-day moving average

## Statistical Forecasting

The project also evaluated:

* ARIMA
* Exponential Smoothing

## Machine Learning

The primary machine-learning models evaluated were:

* Random Forest Regressor
* Gradient Boosting Regressor

Gradient Boosting produced the strongest overall forecasting performance and was therefore used for the multi-horizon forecasting analysis.

# 📊 Multi-Horizon Forecasting

Separate Gradient Boosting models were evaluated for four forecasting horizons:

| Horizon          | MAE    | RMSE   | MAPE   | 100 − MAPE |
| ---------------- | ------ | ------ | ------ | ----------- |
| **1-Day**  | 81.73  | 101.76 | 3.74%  | 96.26%      |
| **7-Day**  | 145.66 | 170.93 | 6.74%  | 93.26%      |
| **14-Day** | 344.23 | 389.87 | 16.00% | 84.00%      |
| **30-Day** | 365.18 | 404.04 | 16.56% | 83.44%      |

The results show that forecast error increases as the planning horizon becomes longer.

The model performs particularly well for short-term forecasting, while 14-day and 30-day forecasts show greater uncertainty and systematic overprediction.

> **Note:** `100 − MAPE` is reported as an error-derived accuracy indicator for interpretability. It should not be interpreted as a conventional classification accuracy metric.

# 📈 Forecast Error & Bias Analysis

Forecast errors were analyzed separately for each horizon.

The model showed relatively low bias for short-term forecasts:

| Horizon | Mean Error | Bias    |
| ------- | ---------- | ------- |
| 1-Day   | -12.15     | -0.54%  |
| 7-Day   | -61.17     | -2.74%  |
| 14-Day  | -310.25    | -13.81% |
| 30-Day  | -236.90    | -10.36% |

Negative error indicates that predicted care load was higher than the observed value.

This indicates an increasing tendency toward  **overprediction at longer horizons** .

# 📐 Forecast Uncertainty

Point forecasts alone do not provide enough information for operational planning.

To estimate uncertainty, the project uses  **empirical residual quantiles** .

For each forecast horizon:

1. Calculate historical forecast residuals.
2. Estimate the 2.5th percentile.
3. Estimate the 97.5th percentile.
4. Add these residual bounds to the point forecast.
5. Produce an approximately 95% prediction interval.

This approach accounts for asymmetric forecast errors and does not require the residuals to follow a normal distribution.

### Empirical Interval Coverage

| Horizon | Approximate Coverage |
| ------- | -------------------- |
| 1-Day   | 93.94%               |
| 7-Day   | 93.88%               |
| 14-Day  | 94.85%               |
| 30-Day  | 93.81%               |

The empirical intervals therefore provide relatively consistent uncertainty coverage across the four forecast horizons.

# ⚠️ Capacity-Risk Analysis

A scenario capacity threshold of **3,000 children** was used to demonstrate capacity-risk monitoring.

The analysis estimates the historical empirical likelihood that forecast uncertainty could extend beyond this threshold.

| Horizon | Mean Estimated Breach Risk | Maximum Estimated Risk |
| ------- | -------------------------- | ---------------------- |
| 1-Day   | 0.00%                      | 0.00%                  |
| 7-Day   | 0.00%                      | 0.00%                  |
| 14-Day  | 0.14%                      | 4.12%                  |
| 30-Day  | 2.07%                      | 22.68%                 |

The results indicate that longer forecast horizons provide greater opportunity to identify  **potential capacity-risk periods** .

### Important Interpretation

These values should be interpreted as  **retrospective empirical risk estimates** , rather than fully calibrated real-time probabilities.

The 3,000-child threshold is also a scenario threshold used for capacity-risk analysis.

The observed evaluation period did **not** reach 3,000 children in HHS care. Therefore, the dashboard identifies  **potential capacity warnings** , rather than confirmed capacity breaches.

# 🚨 Early Warning Analysis

The dashboard uses the upper 95% empirical prediction interval as a warning indicator.

When:

<pre class="overflow-visible! px-0!" data-start="8732" data-end="8787"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-(--code-block-surface) corner-superellipse/1.1 overflow-clip rounded-3xl [--code-block-surface:var(--bg-elevated-secondary)] dark:[--code-block-surface:var(--composer-surface-primary)] lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>Upper Prediction Bound ≥ Capacity Threshold</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

the dashboard identifies a potential capacity warning.

In the evaluation period:

| Horizon | Potential Warning Days |
| ------- | ---------------------- |
| 1-Day   | 0                      |
| 7-Day   | 0                      |
| 14-Day  | 3                      |
| 30-Day  | 18                     |

The earliest potential warning occurred at the  **30-day horizon** , demonstrating how longer forecast horizons can provide additional planning time even when the point forecast itself remains below the capacity threshold.



# 📊 Streamlit Dashboard

The project includes an interactive Streamlit dashboard for exploring the forecasting results.

### Dashboard Features

* 📌 KPI summary cards
* 📈 Actual vs predicted care load
* 🔮 Forecast horizon selection
* 📐 Empirical 95% prediction intervals
* ⚠️ Capacity threshold monitoring
* 📊 Capacity-risk indicators
* 🤖 Model performance comparison
* 📉 Forecast error analysis
* 🔎 Interactive exploration of forecast results

### Live Dashboard

**Streamlit App:**

[predictive-forecasting-hhs-qfberakldqhs7phecsxzzy.streamlit.app](https://predictive-forecasting-hhs-qfberakldqhs7phecsxzzy.streamlit.app/)

# 🛠️ Technology Stack

### Programming

* Python
* Jupyter Notebook

### Data Analysis

* Pandas
* NumPy

### Visualization

* Matplotlib
* Seaborn

### Machine Learning

* Scikit-learn

### Statistical Modeling

* Statsmodels

### Dashboard

* Streamlit

### Development

* VS Code
* Git
* GitHub

# 📁 Project Structure

<pre class="overflow-visible! px-0!" data-start="10076" data-end="10304"><div class="relative w-full mt-4 mb-1"><div class=""><div class="contents"><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-(--code-block-surface) corner-superellipse/1.1 overflow-clip rounded-3xl [--code-block-surface:var(--bg-elevated-secondary)] dark:[--code-block-surface:var(--composer-surface-primary)] lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><pre class="cm-content q9tKkq_readonly m-0"><code><span>Predictive-Forecasting-HHS/
│
├── data/
│   ├── processed/
│   └── raw/
│
├── notebooks/
│
├── src/
│
├── models/
│
├── outputs/
│
├── reports/
│
├── streamlit_app.py
├── requirements.txt
├── README.md
└── .gitignore</span></code></pre></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></div></pre>

Raw data is excluded from version control where appropriate.

# 📊 Project Outputs

The project produces:

* Cleaned operational datasets
* Exploratory analysis
* Engineered forecasting features
* Multi-horizon forecasts
* Model performance metrics
* Forecast residual analysis
* Empirical prediction intervals
* Capacity-risk indicators
* Interactive Streamlit dashboard

# 🔮 Future Enhancements

Potential future improvements include:

* Calendar-aware lag construction for irregular reporting dates
* More robust time-series cross-validation
* Hyperparameter optimization
* External operational and policy variables
* Automated model retraining
* Real-time data integration
* SHAP-based model explainability
* Probabilistic forecasting methods
* Scenario-based capacity simulation
* Monitoring for model drift

# 📜 License

This project is intended for educational and research purposes.


# 👩‍💻 Author

**Shivani**

GitHub:

[https://github.com/shivani1707s](https://github.com/shivani1707s)

⭐ If you found this project useful, consider giving the repository a star!
