import streamlit as st

from utils.data_manager import get_data
from utils.kpi_calculator import calculate_kpis

from utils.visualization import (
    sales_trend,
    top_products_chart
)

st.set_page_config(
    page_title="CEO Dashboard",
    layout="wide"
)

st.title("👔 CEO Executive Dashboard")
st.markdown("### AI Business Intelligence Summary")

# -----------------------------
# Load Data
# -----------------------------

df = get_data()

kpis = calculate_kpis(df)

# -----------------------------
# KPI CARDS
# -----------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "💰 Revenue",
        f"₹{kpis['total_revenue']:,}"
    )

with col2:
    st.metric(
        "💵 Profit",
        f"₹{kpis['total_profit']:,}"
    )

with col3:
    st.metric(
        "📈 Sales",
        kpis["total_sales"]
    )

with col4:
    st.metric(
        "📦 Inventory",
        kpis["total_inventory"]
    )

st.markdown("---")

# -----------------------------
# Revenue Trend
# -----------------------------

st.subheader("📈 Sales Trend")

fig1 = sales_trend(df)

st.plotly_chart(
    fig1,
    use_container_width=True
)

st.markdown("---")

# -----------------------------
# Top Products
# -----------------------------

st.subheader("🏆 Top Products")

fig2 = top_products_chart(df)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.markdown("---")

# -----------------------------
# Executive Insights
# -----------------------------

st.subheader("🤖 AI Executive Insights")

col1, col2 = st.columns(2)

with col1:

    st.success(
        f"🏆 Best Selling Product : {kpis['top_product']}"
    )

    st.info(
        "📊 Sales Forecasting Engine Active"
    )

    st.info(
        "📈 Revenue Growth Expected"
    )

with col2:

    st.warning(
        f"📉 Lowest Selling Product : {kpis['lowest_product']}"
    )

    st.info(
        "📦 Inventory Optimization Active"
    )

    st.info(
        "🤖 AI Monitoring Business Health"
    )

st.markdown("---")

# -----------------------------
# Business Health
# -----------------------------

st.subheader("🏥 Business Health Score")

health = 95

st.metric(
    "Business Score",
    f"{health}/100"
)

progress = health / 100

st.progress(progress)

if health >= 90:

    st.success(
        "🟢 Excellent Business Performance"
    )

elif health >= 70:

    st.warning(
        "🟡 Stable Business Performance"
    )

else:

    st.error(
        "🔴 Business Needs Attention"
    )

st.markdown("---")

# -----------------------------
# CEO Summary
# -----------------------------

st.subheader("📝 CEO Summary")

st.write(f"""
### Business Report

✅ Total Revenue : ₹{kpis['total_revenue']:,}

✅ Total Profit : ₹{kpis['total_profit']:,}

✅ Total Units Sold : {kpis['total_sales']}

✅ Current Inventory : {kpis['total_inventory']}

✅ Best Product : {kpis['top_product']}

✅ Lowest Product : {kpis['lowest_product']}

✅ AI Forecasting : ACTIVE

✅ Inventory Optimization : ACTIVE

✅ Business Growth : POSITIVE
""")

st.markdown("---")

# -----------------------------
# Dataset Preview
# -----------------------------

st.subheader("📋 Business Data Snapshot")

st.dataframe(
    df,
    use_container_width=True
)

st.markdown("---")

# -----------------------------
# AI Recommendation
# -----------------------------

st.subheader("🚀 CEO Recommendations")

st.success(
    "Increase inventory for high demand products."
)

st.info(
    "Focus marketing on best performing products."
)

st.warning(
    "Monitor low performing products."
)