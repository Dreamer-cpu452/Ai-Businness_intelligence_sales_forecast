import streamlit as st

from utils.data_manager import get_data
from utils.forecasting import prepare_data
from utils.forecasting import (
    prepare_data,
    train_model,
    future_prediction,
    evaluate_model
)
from utils.visualization import forecast_chart
from utils.inventory import inventory_recommendation
from utils.forecasting import (
    prepare_data,
    train_model,
    future_prediction,
    evaluate_model,
    predict_revenue_profit
)

st.title("🤖 Sales Forecasting")

df = get_data()

df = prepare_data(df)
model, predictions = train_model(df)
mae, rmse = evaluate_model(
    df,
    predictions
)
future_df = future_prediction(model)

df["Predicted_Sales"] = predictions
predicted_revenue, predicted_profit = predict_revenue_profit(df)
df["Inventory_Status"] = inventory_recommendation(df)

st.success("Dataset Processed Successfully ✅")

st.markdown("---")

st.subheader("📋 Feature Engineered Dataset")

st.dataframe(df)

st.markdown("---")

st.subheader("🧠 Generated Features")

st.write("✔ Year")
st.write("✔ Month")
st.write("✔ Day")

st.info(
    "Machine Learning Training Module Coming Next"
)
st.markdown("---")

st.subheader("🎯 Actual vs Predicted")

st.dataframe(

    df[
        [
            "Date",
            "Units_Sold",
            "Predicted_Sales"
        ]
    ]

)
st.markdown("---")

st.subheader("📈 Forecast Chart")

fig = forecast_chart(df)

st.plotly_chart(
    fig,
    use_container_width=True
)
st.markdown("---")

st.subheader("📦 Inventory Recommendation")

st.dataframe(

    df[
        [
            "Product",
            "Inventory",
            "Predicted_Sales",
            "Inventory_Status"
        ]
    ]

)
st.markdown("---")

st.subheader("🚀 Future Sales Forecast")

st.dataframe(future_df)
st.markdown("---")

st.subheader("📊 Model Performance")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "MAE",
        round(mae, 2)
    )

with col2:
    st.metric(
        "RMSE",
        round(rmse, 2)
    )

st.markdown("---")

if st.button("🚀 Predict Business Outcome"):

    st.subheader("💰 Revenue & Profit Prediction")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Predicted Revenue",
            f"₹{round(predicted_revenue,2)}"
        )

    with col2:

        st.metric(
            "Predicted Profit",
            f"₹{round(predicted_profit,2)}"
        )

    st.markdown("---")

    if predicted_profit > 0:

        st.success(
            "✅ PROFIT EXPECTED"
        )

    else:

        st.error(
            "❌ LOSS EXPECTED"
        )