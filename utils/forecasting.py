import pandas as pd

from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error


def prepare_data(df):

    data = df.copy()

    data["Date"] = pd.to_datetime(data["Date"])

    data["Year"] = data["Date"].dt.year
    data["Month"] = data["Date"].dt.month
    data["Day"] = data["Date"].dt.day

    return data


def train_model(df):

    X = df[
        [
            "Year",
            "Month",
            "Day"
        ]
    ]

    y = df["Units_Sold"]

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(X, y)

    predictions = model.predict(X)

    return model, predictions


def future_prediction(model):

    future = pd.DataFrame({

        "Year": [2026, 2026, 2026],

        "Month": [7, 8, 9],

        "Day": [1, 1, 1]

    })

    future["Predicted_Sales"] = model.predict(

        future[
            [
                "Year",
                "Month",
                "Day"
            ]
        ]

    )

    return future


def evaluate_model(df, predictions):

    actual = df["Units_Sold"]

    mae = mean_absolute_error(
        actual,
        predictions
    )

    rmse = mean_squared_error(
        actual,
        predictions
    ) ** 0.5

    return mae, rmse
def predict_revenue_profit(df):

    predicted_sales = df["Predicted_Sales"]

    avg_price = (
        df["Revenue"] /
        df["Units_Sold"]
    ).mean()

    avg_cost = (
        (df["Revenue"] - df["Profit"])
        /
        df["Units_Sold"]
    ).mean()

    predicted_revenue = (
        predicted_sales * avg_price
    )

    predicted_profit = (
        predicted_sales *
        (avg_price - avg_cost)
    )

    return (
        predicted_revenue.sum(),
        predicted_profit.sum()
    )