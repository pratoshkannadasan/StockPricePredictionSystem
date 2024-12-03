import matplotlib.pyplot as plt

def plot_predictions(train_data, test_data, forecast, forecast_index, stock_symbol):
    plt.figure(figsize=(10, 6))
    plt.plot(train_data, label="Training Data", color="blue")
    plt.plot(test_data, label="Actual Prices", color="green")
    plt.plot(forecast_index, forecast, label="Forecasted Prices", color="red", linestyle="dashed")
    plt.title(f"{stock_symbol} Stock Price Prediction")
    plt.xlabel("Date")
    plt.ylabel("Close Price (USD)")
    plt.legend()
    plt.grid()
    plt.show()

