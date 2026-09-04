import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
# --------------------------------
                
# page configuration
st.set_page_config(
    page_title="HHS Care Load Forecasting",
    page_icon="📊",
    layout="wide"
)            
#---------------------------------------------

# load data
model_df= pd.read_csv(
    "data/processed/model_df.csv"
)

horizon_results_df= pd.read_csv(
    "data/processed/horizon_results_df.csv"
)

all_horizon_predictions_df= pd.read_csv(
    "data/processed/all_horizon_predictions_df.csv"
)

capacity_risk_summary = pd.read_csv(
    "data/processed/capacity_risk_summary.csv"
)
# -----------------------------------------------------------

# Convert dates
model_df["Date"] = pd.to_datetime(
    model_df["Date"]
)

all_horizon_predictions_df["Date"] = pd.to_datetime(
    all_horizon_predictions_df["Date"]
)
# --------------------------------------------------------

# Title
st.title(
    "Predictive Forecasting of Care Load & Placement Demand"
)

st.markdown(
    """
    **HHS Care Load Forecasting Dashboard**

    Forecasting HHS care load using Gradient Boosting,
    multi-horizon prediction, uncertainty estimation,
    and capacity-risk analysis.
    """
)
# -------------------------------------------------------------------

# Siidebar
st.sidebar.header("Forecast Controls")

selected_horizon = st.sidebar.selectbox(
    "Forecast Horizon",
    ["1-Day", "7-Day", "14-Day", "30-Day"]
)

capacity_threshold = st.sidebar.number_input(
    "Capacity Threshold",
    min_value=1000,
    max_value=10000,
    value=3000,
    step=100
)
# --------------------------------------------------

# Select horizon data
horizon_data = all_horizon_predictions_df[
    all_horizon_predictions_df["Horizon"]
    == selected_horizon
].copy()
# --------------------------------------------

# KPI section
st.subheader("Forecast Performance")

kpi_data = horizon_results_df[
    horizon_results_df["Horizon"]
    == selected_horizon
]

if not kpi_data.empty:

    mae = kpi_data["MAE"].iloc[0]
    rmse = kpi_data["RMSE"].iloc[0]
    mape = kpi_data["MAPE"].iloc[0]

    forecast_accuracy = 100 - mape

else:
    mae = 0
    rmse = 0
    mape = 0
    forecast_accuracy = 0
    
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Forecast Accuracy*",
    f"{forecast_accuracy:.2f}%"
)

col2.metric(
    "MAE",
    f"{mae:.2f}"
)

col3.metric(
    "RMSE",
    f"{rmse:.2f}"
)

col4.metric(
    "MAPE",
    f"{mape:.2f}%"
)

st.caption(
    "*Forecast Accuracy is calculated as 100 − MAPE and is "
    "used as an error-derived indicator."
)
# -----------------------------------------------------------------

# Forecast chart
st.subheader(
    f"{selected_horizon} HHS Care Forecast"
)

fig, ax = plt.subplots(
    figsize=(14, 6)
)

ax.plot(
    horizon_data["Date"],
    horizon_data["Actual"],
    label="Actual"
)

ax.plot(
    horizon_data["Date"],
    horizon_data["Predicted"],
    label="Predicted"
)

ax.fill_between(
    horizon_data["Date"],
    horizon_data["Empirical_Lower_95"],
    horizon_data["Empirical_Upper_95"],
    alpha=0.2,
    label="95% Prediction Interval"
)

ax.axhline(
    capacity_threshold,
    linestyle="--",
    label="Capacity Threshold"
)

ax.set_xlabel("Date")

ax.set_ylabel(
    "Children in HHS Care"
)

ax.set_title(
    f"{selected_horizon} Forecast with Empirical 95% Prediction Interval"
)

ax.legend()

ax.grid(
    True,
    alpha=0.3
)

plt.xticks(
    rotation=45
)

plt.tight_layout()

st.pyplot(fig)
#----------------------------------------------------------------------

# Capacity risk
st.subheader("Capacity-Breach Risk")

risk_data = capacity_risk_summary[
    capacity_risk_summary["Horizon"]
    == selected_horizon
]

if not risk_data.empty:
    mean_risk = risk_data[
            "Mean_Breach_Probability"
        ].iloc[0]
    
    maximum_risk = risk_data[
        "Maximum_Breach_Probability"
    ].iloc[0]

else:
    mean_risk = 0
    maximum_risk = 0
    
risk_col1, risk_col2 = st.columns(2)

risk_col1.metric(
    "Mean Capacity-Breach Risk",
    f"{mean_risk:.2f}%"
)

risk_col2.metric(
    "Maximum Capacity-Breach Risk",
    f"{maximum_risk:.2f}%"
)

st.info(
    """
    Capacity-breach risk is an empirical risk indicator derived
    from the historical residual distribution. It should not be
    interpreted as a fully calibrated probability forecast.
    """
)
# ------------------------------------------------------------------------

# Model comparison
st.subheader("Model Performance by Forecast Horizon")

display_results = horizon_results_df.copy()

display_results["Forecast Accuracy (%)"] = (
    100 - display_results["MAPE"]
)

st.dataframe(
    display_results,
    use_container_width=True
)
# ------------------------------------------------------------

# Error by horizon
st.subheader("Forecast Error by Horizon")

fig2, ax2 = plt.subplots(
    figsize=(10, 5)
)

ax2.plot(
    horizon_results_df["Horizon"],
    horizon_results_df["MAPE"],
    marker="o"
)

ax2.set_xlabel(
    "Forecast Horizon"
)

ax2.set_ylabel(
    "MAPE (%)"
)

ax2.set_title(
    "Forecast Error Increases with Prediction Horizon"
)

ax2.grid(
    True,
    alpha=0.3
)

plt.tight_layout()

st.pyplot(fig2)
# ------------------------------------------------------------------

# Footer
st.markdown("---")

st.caption(
    "Predictive Forecasting of Care Load & Placement Demand | "
    "HHS / UAC Program"
)