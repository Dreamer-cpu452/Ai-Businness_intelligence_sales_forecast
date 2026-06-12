def inventory_recommendation(df):

    recommendations = []

    for _, row in df.iterrows():

        if row["Inventory"] < row["Predicted_Sales"]:

            recommendations.append(
                "Restock"
            )

        elif row["Inventory"] > row["Predicted_Sales"] * 2:

            recommendations.append(
                "Overstock"
            )

        else:

            recommendations.append(
                "Optimal"
            )

    return recommendations


def stock_risk(df):

    risks = []

    for _, row in df.iterrows():

        if row["Inventory_Status"] == "Restock":

            risks.append(
                "High Risk"
            )

        elif row["Inventory_Status"] == "Overstock":

            risks.append(
                "Medium Risk"
            )

        else:

            risks.append(
                "Low Risk"
            )

    return risks