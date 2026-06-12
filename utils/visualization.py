import plotly.express as px


# ---------------------------------
# Sales Analysis
# ---------------------------------

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


# ---------------------------------
# Forecasting
# ---------------------------------

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


# ---------------------------------
# Segmentation
# ---------------------------------

def segment_chart(df):

    fig = px.scatter(
        df,
        x="Revenue",
        y="Profit",
        color="Segment",
        size="Units_Sold",
        hover_name="Product",
        title="Product Segmentation"
    )

    return fig


# ---------------------------------
# Dashboard
# ---------------------------------

def sales_trend(df):

    fig = px.line(
        df,
        x="Date",
        y="Units_Sold",
        markers=True,
        title="Sales Trend"
    )

    return fig


def revenue_distribution(df):

    fig = px.pie(
        df,
        names="Product",
        values="Revenue",
        title="Revenue Distribution"
    )

    return fig


def profit_distribution(df):

    fig = px.bar(
        df,
        x="Product",
        y="Profit",
        color="Product",
        title="Profit Distribution"
    )

    return fig


# ---------------------------------
# Product Performance
# ---------------------------------

def revenue_vs_profit(df):

    fig = px.scatter(
        df,
        x="Revenue",
        y="Profit",
        size="Units_Sold",
        color="Product",
        hover_name="Product",
        title="Revenue vs Profit"
    )

    return fig


def top_products_chart(df):

    summary = (
        df.groupby("Product")["Revenue"]
        .sum()
        .reset_index()
    )

    summary = summary.sort_values(
        by="Revenue",
        ascending=False
    )

    fig = px.bar(
        summary,
        x="Revenue",
        y="Product",
        orientation="h",
        color="Revenue",
        title="Top Products"
    )

    return fig


def product_compare(df):

    fig = px.line(
        df,
        x="Product",
        y=[
            "Revenue",
            "Profit"
        ],
        markers=True,
        title="Revenue vs Profit Comparison"
    )

    return fig


# ---------------------------------
# Inventory
# ---------------------------------

def inventory_status_chart(df):

    summary = (
        df["Inventory_Status"]
        .value_counts()
        .reset_index()
    )

    summary.columns = [
        "Status",
        "Count"
    ]

    fig = px.pie(
        summary,
        names="Status",
        values="Count",
        title="Inventory Status"
    )

    return fig


def risk_chart(df):

    summary = (
        df["Risk_Level"]
        .value_counts()
        .reset_index()
    )

    summary.columns = [
        "Risk",
        "Count"
    ]

    fig = px.bar(
        summary,
        x="Risk",
        y="Count",
        color="Risk",
        title="Inventory Risk"
    )

    return fig