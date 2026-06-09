import pandas as pd


def save_forecast(forecast, data):
    result = forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail(60).copy()

    latest_price = None
    if data is not None and not data.empty and "Close" in data.columns:
        close_series = data["Close"].dropna()
        last_value = close_series.iloc[-1]
        latest_price = float(last_value.item()) if hasattr(last_value, "item") else float(last_value)

    result["Today\'s Price"] = latest_price

    result = result.rename(columns={
        "ds": "Date",
        "yhat": "Forecasted Price",
        "yhat_lower": "Lower Bound",
        "yhat_upper": "Upper Bound"
    })
    result.to_excel("reports/monthly_forecast.xlsx", index=False)
    result.to_csv("reports/monthly_forecast.csv", index=False)
    return result
