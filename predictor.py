from prophet import Prophet


def predict_next_5_years(df):
    data = df.reset_index()
    data = data[["Date", "Close"]]
    data.columns = ["ds", "y"]

    model = Prophet()
    model.fit(data)

    future = model.make_future_dataframe(periods=60, freq="ME")
    forecast = model.predict(future)
    return forecast
