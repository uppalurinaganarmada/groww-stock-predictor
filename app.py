from stock_mapping import STOCK_MAPPING
from data_fetcher import fetch_stock_data
from predictor import predict_next_5_years
from report_generator import save_forecast

stock_name = input("Enter Stock Name from Groww: ")

if stock_name not in STOCK_MAPPING:
    print("Stock not found")
    exit()

ticker = STOCK_MAPPING[stock_name]

print("Downloading data...")

data = fetch_stock_data(ticker)

print("Predicting...")

forecast = predict_next_5_years(data)
result = save_forecast(forecast)

print(result)
