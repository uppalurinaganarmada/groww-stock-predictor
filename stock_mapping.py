STOCK_MAPPING = {
    "Reliance Industries": "RELIANCE.NS",
    "Tata Motors": "TATAMOTORS.NS",
    "Infosys": "INFY.NS",
    "HDFC Bank": "HDFCBANK.NS",
    "ICICI Bank": "ICICIBANK.NS"
}


def normalize_name(name):
    return "".join(char.lower() for char in name if char.isalnum())


def get_ticker(stock_name):
    query = normalize_name(stock_name)

    for display_name, ticker in STOCK_MAPPING.items():
        normalized_display = normalize_name(display_name)

        if query == normalized_display or query in normalized_display or normalized_display.startswith(query):
            return ticker

    return None
