import streamlit as st

from utils.data_manager import get_data

from utils.visualization import (
    sales_by_product,
    revenue_by_product,
    profit_by_product,
    revenue_vs_profit,
    top_products_chart,
    product_compare
)

st.title("🔥 Product Performance Dashboard")

# ---------------------------------
# Load Data
# ---------------------------------

df = get_data()

# ---------------------------------
# Product Statistics
# ---------------------------------

best_product = df.loc[
    df["Units_Sold"].idxmax()
]

worst_product = df.loc[
    df["Units_Sold"].idxmin()
]

highest_revenue = df.loc[
    df["Revenue"].idxmax()
]

highest_profit = df.loc[
    df["Profit"].idxmax()
]

# ---------------------------------
# KPI Cards
# ---------------------------------

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

# ---------------------------------
# Sales Graph
# ---------------------------------

st.subheader("📈 Sales by Product")

fig1 = sales_by_product(df)

st.plotly_chart(
    fig1,
    use_container_width=True
)

st.markdown("---")

# ---------------------------------
# Revenue Graph
# ---------------------------------

st.subheader("💰 Revenue by Product")

fig2 = revenue_by_product(df)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.markdown("---")

# ---------------------------------
# Profit Graph
# ---------------------------------

st.subheader("💵 Profit by Product")

fig3 = profit_by_product(df)

st.plotly_chart(
    fig3,
    use_container_width=True
)

st.markdown("---")

# ---------------------------------
# Revenue vs Profit
# ---------------------------------

st.subheader("🎯 Revenue vs Profit")

fig4 = revenue_vs_profit(df)

st.plotly_chart(
    fig4,
    use_container_width=True
)

st.markdown("---")

# ---------------------------------
# Top Products
# ---------------------------------

st.subheader("🏅 Top Products")

fig5 = top_products_chart(df)

st.plotly_chart(
    fig5,
    use_container_width=True
)

st.markdown("---")

# ---------------------------------
# Product Comparison
# ---------------------------------

st.subheader("📊 Product Comparison")

fig6 = product_compare(df)

st.plotly_chart(
    fig6,
    use_container_width=True
)

st.markdown("---")

# ---------------------------------
# AI Insights
# ---------------------------------

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
    "📦 AI recommends increasing inventory for high-demand products."
)

st.markdown("---")

# ---------------------------------
# Dataset
# ---------------------------------

st.subheader("📋 Product Dataset")

st.dataframe(
    df,
    use_container_width=True
)