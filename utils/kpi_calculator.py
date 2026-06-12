def calculate_kpis(df):

    total_sales = df["Units_Sold"].sum()
    total_revenue = df["Revenue"].sum()
    total_profit = df["Profit"].sum()
    total_inventory = df["Inventory"].sum()

    average_sales = df["Units_Sold"].mean()
    average_profit = df["Profit"].mean()

    top_product = df.loc[
        df["Units_Sold"].idxmax(),
        "Product"
    ]

    lowest_product = df.loc[
        df["Units_Sold"].idxmin(),
        "Product"
    ]

    return {

        "total_sales": total_sales,

        "total_revenue": total_revenue,

        "total_profit": total_profit,

        "total_inventory": total_inventory,

        "average_sales": average_sales,

        "average_profit": average_profit,

        "top_product": top_product,

        "lowest_product": lowest_product

    }