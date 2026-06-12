def generate_recommendation(df):

    recommendations = []

    for _, row in df.iterrows():

        if row["Inventory_Status"] == "Restock":

            recommendations.append(

                f"Increase inventory for {row['Product']}"

            )

        elif row["Inventory_Status"] == "Overstock":

            recommendations.append(

                f"Reduce inventory for {row['Product']}"

            )

        else:

            recommendations.append(

                f"Maintain inventory for {row['Product']}"

            )

    return recommendations