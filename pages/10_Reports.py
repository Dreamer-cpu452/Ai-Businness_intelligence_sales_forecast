import streamlit as st

from utils.data_manager import get_data
from utils.kpi_calculator import calculate_kpis

st.title("📄 Business Report Dashboard")

# ---------------------------------
# Load Data
# ---------------------------------

df = get_data()

kpis = calculate_kpis(df)

# ---------------------------------
# KPI Summary
# ---------------------------------

st.subheader("📊 Business Summary")

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "📈 Total Sales",
        kpis["total_sales"]
    )

    st.metric(
        "💰 Total Revenue",
        f"₹{kpis['total_revenue']:,}"
    )

with col2:

    st.metric(
        "💵 Total Profit",
        f"₹{kpis['total_profit']:,}"
    )

    st.metric(
        "📦 Inventory",
        kpis["total_inventory"]
    )

st.markdown("---")

# ---------------------------------
# Product Insights
# ---------------------------------

st.subheader("🤖 AI Report")

st.success(
    f"🏆 Best Product : {kpis['top_product']}"
)

st.warning(
    f"📉 Lowest Product : {kpis['lowest_product']}"
)

st.info(
    "📊 Sales Forecasting Module Active"
)

st.info(
    "📦 Inventory Optimization Module Active"
)

st.markdown("---")

# ---------------------------------
# Dataset Preview
# ---------------------------------

st.subheader("📋 Business Dataset")

st.dataframe(
    df,
    use_container_width=True
)

st.markdown("---")

# ---------------------------------
# CSV Download
# ---------------------------------

st.subheader("📥 Export Report")

csv = df.to_csv(
    index=False
)

st.download_button(

    label="⬇ Download CSV Report",

    data=csv,

    file_name="business_report.csv",

    mime="text/csv",

    key="business_csv_download"

)