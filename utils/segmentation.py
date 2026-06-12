from sklearn.cluster import KMeans


def product_segmentation(df):

    X = df[
        [
            "Revenue",
            "Profit",
            "Units_Sold"
        ]
    ]

    model = KMeans(
        n_clusters=3,
        random_state=42,
        n_init=10
    )

    df["Segment"] = model.fit_predict(X)

    return df