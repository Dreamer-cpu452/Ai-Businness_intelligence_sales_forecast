import streamlit as st

from utils.data_manager import get_data
from utils.kpi_calculator import calculate_kpis

st.title("📄 Business Report")

df = get_data()

kpis = calculate_kpis(df)

st.subheader("Business Summary")

st.write(f"Total Sales : {kpis['total_sales']}")

st.write(f"Total Revenue : ₹{kpis['total_revenue']:,}")

st.write(f"Total Profit : ₹{kpis['total_profit']:,}")

st.write(f"Best Product : {kpis['top_product']}")

st.write(f"Lowest Product : {kpis['lowest_product']}")

st.markdown("---")

st.dataframe(df)