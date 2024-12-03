Stock Price Prediction System
This project is a Stock Price Prediction system that uses machine learning models to predict stock prices and provides real-time alerts when a stock price crosses a specified threshold. It includes two models, ARIMA and LSTM, and visualizes the results. The system also allows the user to receive notifications when the stock price exceeds or falls below the defined threshold.

Features
Stock Price Prediction: Predict future stock prices using ARIMA and LSTM models.
Real-Time Alerts: Send email alerts when the stock price reaches a specified threshold.
Multiple Models: ARIMA and LSTM models for comparison.
Visualization: Graphical representation of predicted and actual stock prices.
Configurable: Easily configurable stock symbol, start date, end date, and alert thresholds.
Project Structure
plaintext
Copy code
stock_price_prediction/
├── main.py                   # Main entry point
├── config.py                 # Configuration file
├── models/                   # Directory for model implementations
│   ├── arima_model.py        # ARIMA model implementation
│   └── lstm_model.py         # LSTM model implementation
├── alerts/                   # Directory for alerts
│   └── price_alert.py        # Price alert system
├── utils/                    # Utility functions (e.g., data fetching, preprocessing)
│   ├── data_fetcher.py       # Fetch stock data
│   └── visualizer.py         # Visualization functions
├── requirements.txt          # Dependencies
└── README.md                 # Project overview
Requirements
This project requires the following Python libraries:

yfinance: To fetch stock data.
pandas: For data manipulation and analysis.
numpy: For numerical operations.
matplotlib: For plotting graphs.
statsmodels: For ARIMA model implementation.
scikit-learn: For model evaluation.
tensorflow: For building the LSTM model.
Install the required dependencies using the following command:

bash
Copy code
pip install -r requirements.txt
Setup and Configuration
Clone or download the repository to your local machine.

Install all dependencies using the command:

bash
Copy code
pip install -r requirements.txt
Configure the parameters by editing the config.py file:

python
Copy code
STOCK_SYMBOL = "AAPL"  # Stock symbol (e.g., AAPL for Apple)
START_DATE = "2015-01-01"  # Start date for stock data
END_DATE = "2023-12-31"  # End date for stock data
THRESHOLD_PRICE = 150  # Threshold price for sending alerts
You may also need to update the email configurations in the alerts/price_alert.py file:

python
Copy code
sender_email = "your_email@example.com"
receiver_email = "receiver_email@example.com"
password = "your_email_password"
How It Works
Data Fetching: The system fetches historical stock data using the yfinance library. The data is fetched based on the symbol, start date, and end date defined in the config.py file.

Model Training:

ARIMA: The ARIMA model is used for time-series forecasting. It is trained on historical stock prices, and predictions are made for the test set.
LSTM: The LSTM (Long Short-Term Memory) model is a deep learning model that is trained on the stock data and predicts future prices based on historical trends.
Model Prediction: The system predicts the stock prices using both ARIMA and LSTM models. The predictions are then compared to the actual values for evaluation.

Visualization: The predicted prices and the actual prices are plotted using matplotlib for easy comparison.

Alerts: The system checks if the stock price exceeds or falls below a predefined threshold. If the condition is met, an email alert is sent.

Running the Project
To run the project, simply execute the main.py file:

bash
Copy code
python main.py
This will:

Fetch the stock data.
Train the ARIMA and LSTM models.
Generate predictions and visualizations.
Check if the stock price crosses the alert threshold and send an email if needed.
Example Output
Stock Price Predictions: The system will print and plot the predictions for stock prices. You will see graphs comparing predicted vs. actual stock prices.

Email Alerts: If the stock price crosses the threshold, an email will be sent to the configured email address.

Customization
Change the STOCK_SYMBOL in the config.py file to any valid stock symbol (e.g., "GOOG" for Google).
Modify the THRESHOLD_PRICE in config.py to set your desired alert price.
You can also adjust the machine learning model configurations (e.g., ARIMA order or LSTM hyperparameters) in the respective model files.
Dependencies
To install the dependencies, run:

bash
Copy code
pip install -r requirements.txt
The requirements.txt file includes all the necessary libraries for the project:

plaintext
Copy code
yfinance
pandas
numpy
matplotlib
statsmodels
scikit-learn
tensorflow