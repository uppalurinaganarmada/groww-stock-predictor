from stock_mapping import get_ticker
from data_fetcher import fetch_stock_data
from predictor import predict_next_5_years
from report_generator import save_forecast

stock_name = input("Enter Stock Name from Groww: ")

ticker = get_ticker(stock_name)

if ticker is None:
    print("Stock not found")
    exit()

print("Downloading data...")

data = fetch_stock_data(ticker)

print("Predicting...")

forecast = predict_next_5_years(data)
result = save_forecast(forecast, data)

print(result)
