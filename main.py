import pandas as pd
from config import STOCK_SYMBOL, START_DATE, END_DATE, THRESHOLD_PRICE
from utils.data_fetcher import fetch_stock_data
from models.arima_model import train_arima_model, forecast_arima
from models.lstm_model import preprocess_data, build_lstm_model, train_lstm_model, forecast_lstm
from utils.visualizer import plot_predictions
from alerts.price_alert import send_alert_email

# Fetch data
data = fetch_stock_data(STOCK_SYMBOL, START_DATE, END_DATE)

# Split data into training and test sets
train_size = int(len(data) * 0.8)
train_data, test_data = data[:train_size], data[train_size:]

# ARIMA model
arima_model = train_arima_model(train_data)
arima_forecast = forecast_arima(arima_model, len(test_data))
plot_predictions(train_data, test_data, arima_forecast, test_data.index, STOCK_SYMBOL)

# LSTM model
x_train, y_train, scaler = preprocess_data(train_data)
lstm_model = build_lstm_model(x_train)
train_lstm_model(lstm_model, x_train, y_train)
x_test, _ = preprocess_data(test_data)
lstm_forecast = forecast_lstm(lstm_model, x_test, scaler)
plot_predictions(train_data, test_data, lstm_forecast, test_data.index, STOCK_SYMBOL)

# Alerts
if test_data['Close'].iloc[-1] > THRESHOLD_PRICE:
    send_alert_email(test_data['Close'].iloc[-1], THRESHOLD_PRICE, STOCK_SYMBOL)
