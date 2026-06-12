import streamlit as st

st.title("⚙ System Settings")

currency = st.selectbox(

    "Currency",

    [
        "INR",
        "USD"
    ]

)

forecast_days = st.slider(

    "Forecast Months",

    1,

    12,

    3

)

model = st.selectbox(

    "Machine Learning Model",

    [
        "Random Forest",
        "Linear Regression (Future)",
        "XGBoost (Future)"
    ]

)

st.markdown("---")

st.subheader("Current Configuration")

st.write(
    f"Currency : {currency}"
)

st.write(
    f"Forecast Months : {forecast_days}"
)

st.write(
    f"Model : {model}"
)

st.success(
    "Configuration Loaded Successfully ✅"
)