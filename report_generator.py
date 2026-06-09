import pandas as pd


def save_forecast(forecast):
    result = forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail(60)
    result.to_excel("reports/monthly_forecast.xlsx", index=False)
    result.to_csv("reports/monthly_forecast.csv", index=False)
    return result
