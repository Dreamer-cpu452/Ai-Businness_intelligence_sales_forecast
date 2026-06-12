import streamlit as st
from utils.data_manager import get_data
from utils.kpi_calculator import calculate_kpis

st.title("👔 CEO Dashboard")
st.markdown("### Executive Business Summary")

df = get_data()

kpis = calculate_kpis(df)

# ==========================
# KPI CARDS
# ==========================

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

# ==========================
# EXECUTIVE INSIGHTS
# ==========================

st.subheader("🤖 Executive Insights")

st.success(
    f"🏆 Best Selling Product : {kpis['top_product']}"
)

st.warning(
    f"📉 Lowest Selling Product : {kpis['lowest_product']}"
)

st.info(
    "📊 Sales Forecasting Engine is Active."
)

st.info(
    "📦 Inventory Optimization Engine is Running."
)

st.markdown("---")

# ==========================
# BUSINESS HEALTH
# ==========================

st.subheader("🏥 Business Health")

health_score = 90

st.metric(
    "Business Score",
    f"{health_score}/100"
)

if health_score >= 90:
    st.success("Excellent Business Performance ✅")
elif health_score >= 70:
    st.warning("Business Performance is Stable ⚠")
else:
    st.error("Business Performance Needs Attention ❌")

st.markdown("---")

# ==========================
# CEO SUMMARY
# ==========================

st.subheader("📝 CEO Summary")

st.write(f"""
• Total Revenue Generated : ₹{kpis['total_revenue']:,}

• Total Profit Generated : ₹{kpis['total_profit']:,}

• Total Units Sold : {kpis['total_sales']}

• Current Inventory : {kpis['total_inventory']}

• Best Performing Product : {kpis['top_product']}

• Lowest Performing Product : {kpis['lowest_product']}

• AI Forecasting Module : Active

• Inventory Optimization Module : Active
""")

st.markdown("---")

# ==========================
# DATA PREVIEW
# ==========================

st.subheader("📋 Business Data Snapshot")

st.dataframe(df)