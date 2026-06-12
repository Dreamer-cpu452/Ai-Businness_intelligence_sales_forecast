import streamlit as st
from utils.data_manager import get_data

st.title("🔥 Product Performance")

df = get_data()

# ------------------------
# Product Statistics
# ------------------------

best_product = df.loc[df["Units_Sold"].idxmax()]
worst_product = df.loc[df["Units_Sold"].idxmin()]
highest_revenue = df.loc[df["Revenue"].idxmax()]
highest_profit = df.loc[df["Profit"].idxmax()]

# ------------------------
# KPI Cards
# ------------------------

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "🏆 Best Selling Product",
        best_product["Product"]
    )

with col2:
    st.metric(
        "📉 Lowest Selling Product",
        worst_product["Product"]
    )

col3, col4 = st.columns(2)

with col3:
    st.metric(
        "💰 Highest Revenue Product",
        highest_revenue["Product"]
    )

with col4:
    st.metric(
        "💵 Highest Profit Product",
        highest_profit["Product"]
    )

st.markdown("---")

st.subheader("📋 Product Performance Data")

st.dataframe(df)
st.markdown("---")

st.subheader("🤖 AI Product Insights")

st.success(
    f"🔥 {best_product['Product']} is the best selling product."
)

st.warning(
    f"📉 {worst_product['Product']} has the lowest demand."
)

st.info(
    f"💰 {highest_revenue['Product']} generates maximum revenue."
)

st.info(
    f"💵 {highest_profit['Product']} gives maximum profit."
)

st.success(
    "📦 Inventory optimization recommendations will be generated after forecasting."
)
st.markdown("---")

st.subheader("🤖 AI Product Insights")

st.success(
    f"🔥 {best_product['Product']} is the best selling product."
)

st.warning(
    f"📉 {worst_product['Product']} has the lowest demand."
)

st.info(
    f"💰 {highest_revenue['Product']} generates maximum revenue."
)

st.info(
    f"💵 {highest_profit['Product']} generates maximum profit."
)

st.success(
    "📦 Inventory recommendations will be generated after forecasting."
)