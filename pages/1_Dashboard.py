import streamlit as st

from utils.data_manager import get_data
from utils.kpi_calculator import calculate_kpis
from utils.visualization import (
    sales_trend,
    revenue_distribution,
    top_products_chart
)

st.title("📊 Business Dashboard")

df = get_data()

kpis = calculate_kpis(df)

total_sales = kpis["total_sales"]
total_revenue = kpis["total_revenue"]
total_profit = kpis["total_profit"]
total_inventory = kpis["total_inventory"]

# KPI Cards

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Sales", total_sales)

with col2:
    st.metric("Revenue", f"₹{total_revenue:,}")

with col3:
    st.metric("Profit", f"₹{total_profit:,}")

with col4:
    st.metric("Inventory", total_inventory)

st.markdown("---")

st.subheader("📋 Sales Data Preview")

st.dataframe(df.head())

st.markdown("---")

st.subheader("🤖 Quick Business Insights")

st.success(
    f"🔥 Best Selling Product : {kpis['top_product']}"
)

st.info(
    f"📉 Lowest Selling Product : {kpis['lowest_product']}"
)

st.info(
    f"💰 Total Revenue : ₹{total_revenue:,}"
)

st.warning(
    "📦 Inventory Optimization Module Coming Soon"
)
st.markdown("---")

st.subheader("📈 Revenue Trend")

fig1 = sales_trend(df)

st.plotly_chart(
    fig1,
    use_container_width=True
)

st.markdown("---")

st.subheader("🛒 Revenue Distribution")

fig2 = revenue_distribution(df)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.markdown("---")

st.subheader("🏆 Top Products")

fig3 = top_products_chart(df)

st.plotly_chart(
    fig3,
    use_container_width=True
)