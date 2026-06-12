import streamlit as st

from utils.data_manager import get_data

from utils.visualization import (

    sales_trend,

    revenue_distribution,

    profit_distribution

)

st.title("📊 Data Analysis")

df = get_data()

st.success("Dataset Loaded Successfully")

st.markdown("---")

# KPI

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(

        "Products",

        len(df)

    )

with col2:

    st.metric(

        "Total Revenue",

        f"₹{df['Revenue'].sum():,.0f}"

    )

with col3:

    st.metric(

        "Total Profit",

        f"₹{df['Profit'].sum():,.0f}"

    )

st.markdown("---")

st.subheader("📈 Sales Trend")

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

st.subheader("📊 Profit Distribution")

fig3 = profit_distribution(df)

st.plotly_chart(

    fig3,

    use_container_width=True

)

st.markdown("---")

st.subheader("📋 Dataset Preview")

st.dataframe(df)