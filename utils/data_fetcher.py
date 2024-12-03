import yfinance as yf

def fetch_stock_data(stock_symbol, start_date, end_date):
    data = yf.download(stock_symbol, start=start_date, end=end_date)
    data = data['Close'].to_frame()  # Only closing price
    data.columns = ['Close']
    data.dropna(inplace=True)
    return data
