import streamlit as st

from utils.data_manager import get_data
from utils.kpi_calculator import calculate_kpis
from utils.forecasting import (
    prepare_data,
    train_model
)
from utils.inventory import inventory_recommendation

st.title("🤖 AI Business Assistant")

df = get_data()

df = prepare_data(df)

model, predictions = train_model(df)

df["Predicted_Sales"] = predictions

df["Inventory_Status"] = inventory_recommendation(df)

kpis = calculate_kpis(df)

question = st.text_input(
    "Ask a business question"
)

if question:

    q = question.lower()

    if "best" in q:

        st.success(
            f"🏆 Best Selling Product : {kpis['top_product']}"
        )

    elif "lowest" in q:

        st.warning(
            f"📉 Lowest Selling Product : {kpis['lowest_product']}"
        )

    elif "revenue" in q:

        st.info(
            f"💰 Total Revenue : ₹{kpis['total_revenue']:,}"
        )

    elif "profit" in q:

        st.info(
            f"💵 Total Profit : ₹{kpis['total_profit']:,}"
        )

    elif "sales" in q:

        st.info(
            f"📊 Total Sales : {kpis['total_sales']}"
        )

    elif "inventory" in q:

        st.dataframe(
            df[
                [
                    "Product",
                    "Inventory_Status"
                ]
            ]
        )

    elif "help" in q:

        st.write("""
Available Questions

• best product

• lowest product

• revenue

• profit

• sales

• inventory
        """)

    else:

        st.error(
            "I don't understand that question yet. Type 'help'."
        )