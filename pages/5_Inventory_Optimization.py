import streamlit as st

from utils.data_manager import get_data
from utils.forecasting import (
    prepare_data,
    train_model
)

from utils.inventory import (
    inventory_recommendation,
    stock_risk
)
from utils.ai_insights import generate_recommendation
from utils.inventory import inventory_recommendation

st.title("📦 Inventory Optimization")

df = get_data()

df = prepare_data(df)

model, predictions = train_model(df)

df["Predicted_Sales"] = predictions

df["Inventory_Status"] = inventory_recommendation(df)
df["Risk_Level"] = stock_risk(df)
df["AI_Recommendation"] = generate_recommendation(df)

st.success("Inventory Engine Loaded Successfully ✅")

st.markdown("---")

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

st.subheader("🤖 AI Inventory Insights")

restock = len(
    df[
        df["Inventory_Status"] == "Restock"
    ]
)

overstock = len(
    df[
        df["Inventory_Status"] == "Overstock"
    ]
)

optimal = len(
    df[
        df["Inventory_Status"] == "Optimal"
    ]
)

st.success(
    f"✅ Optimal Products : {optimal}"
)

st.warning(
    f"⚠ Restock Required : {restock}"
)

st.error(
    f"❌ Overstock Products : {overstock}"
)
st.markdown("---")

st.subheader("⚠ Inventory Risk Analysis")

st.dataframe(

    df[
        [
            "Product",
            "Inventory_Status",
            "Risk_Level"
        ]
    ]

)
st.markdown("---")

st.subheader("🤖 AI Recommendations")

st.dataframe(

    df[
        [
            "Product",
            "AI_Recommendation"
        ]
    ]

)