import streamlit as st

from utils.data_manager import get_data
from utils.forecasting import (
    prepare_data,
    train_model
)
from utils.inventory import inventory_recommendation

st.title("🧠 AI Business Insights")

df = get_data()

df = prepare_data(df)

model, predictions = train_model(df)

df["Predicted_Sales"] = predictions

df["Inventory_Status"] = inventory_recommendation(df)

st.subheader("🤖 AI Business Summary")

best = df.loc[
    df["Units_Sold"].idxmax(),
    "Product"
]

worst = df.loc[
    df["Units_Sold"].idxmin(),
    "Product"
]

highest_profit = df.loc[
    df["Profit"].idxmax(),
    "Product"
]

st.success(
    f"🏆 Best Selling Product : {best}"
)

st.warning(
    f"📉 Lowest Selling Product : {worst}"
)

st.info(
    f"💰 Highest Profit Product : {highest_profit}"
)

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

st.markdown("---")

st.subheader("📦 Inventory Insights")

st.write(
    f"Products to Restock : {restock}"
)

st.write(
    f"Overstock Products : {overstock}"
)

st.markdown("---")

st.subheader("💡 AI Recommendations")

st.write("• Increase stock for high demand products.")

st.write("• Reduce inventory for overstocked products.")

st.write("• Monitor future sales predictions regularly.")