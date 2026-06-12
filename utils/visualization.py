import plotly.express as px


def sales_by_product(df):

    fig = px.bar(
        df,
        x="Product",
        y="Units_Sold",
        color="Product",
        title="Sales by Product"
    )

    return fig


def revenue_by_product(df):

    fig = px.bar(
        df,
        x="Product",
        y="Revenue",
        color="Product",
        title="Revenue by Product"
    )

    return fig


def inventory_by_product(df):

    fig = px.bar(
        df,
        x="Product",
        y="Inventory",
        color="Product",
        title="Inventory by Product"
    )

    return fig


def profit_by_product(df):

    fig = px.bar(
        df,
        x="Product",
        y="Profit",
        color="Product",
        title="Profit by Product"
    )

    return fig


def units_vs_inventory(df):

    fig = px.scatter(
        df,
        x="Units_Sold",
        y="Inventory",
        color="Product",
        size="Revenue",
        title="Sales vs Inventory"
    )

    return fig

def forecast_chart(df):

    fig = px.line(

        df,

        x="Date",

        y=[
            "Units_Sold",
            "Predicted_Sales"
        ],

        title="Actual vs Predicted Sales"

    )

    return fig