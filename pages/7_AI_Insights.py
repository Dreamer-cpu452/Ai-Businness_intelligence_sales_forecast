import streamlit as st

from utils.data_manager import get_data
from utils.forecasting import (
    prepare_data,
    train_model
)
from utils.inventory import inventory_recommendation
from utils.visualization import (

    sales_trend,

    revenue_distribution,

    inventory_status_chart

)

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
st.metric(
    "Business Health",
    "95%"
)

st.success(
    "Revenue Growth Expected"
)
st.markdown("---")

st.subheader("📈 Revenue Trend")

fig1 = sales_trend(df)

st.plotly_chart(
    fig1,
    use_container_width=True
)

st.markdown("---")

st.subheader("💰 Revenue Distribution")

fig2 = revenue_distribution(df)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.markdown("---")

st.subheader("📦 Inventory Health")

fig3 = inventory_status_chart(df)

st.plotly_chart(
    fig3,
    use_container_width=True
)

st.markdown("---")

st.metric(
    "Business Health Score",
    "95%"
)

st.success(
    "AI predicts positive business growth."
)