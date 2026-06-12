import streamlit as st

from utils.data_manager import get_data

from utils.visualization import (
    sales_by_product,
    revenue_by_product,
    inventory_by_product,
    profit_by_product,
    units_vs_inventory
)

st.title("📈 Sales Analysis")

df = get_data()

st.success("Dataset Loaded Successfully ✅")

st.markdown("---")

st.subheader("📊 Sales by Product")

fig1 = sales_by_product(df)

st.plotly_chart(fig1, use_container_width=True)

st.markdown("---")

st.subheader("💰 Revenue by Product")

fig2 = revenue_by_product(df)

st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

st.subheader("📦 Inventory by Product")

fig3 = inventory_by_product(df)

st.plotly_chart(fig3, use_container_width=True)
st.markdown("---")

st.subheader("💵 Profit by Product")

fig4 = profit_by_product(df)

st.plotly_chart(
    fig4,
    use_container_width=True
)

st.markdown("---")

st.subheader("📊 Sales vs Inventory")

fig5 = units_vs_inventory(df)

st.plotly_chart(
    fig5,
    use_container_width=True
)