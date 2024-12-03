from statsmodels.tsa.arima.model import ARIMA
import numpy as np
from sklearn.metrics import mean_squared_error

def train_arima_model(train_data):
    model = ARIMA(train_data, order=(5, 1, 0))
    model_fit = model.fit()
    return model_fit

def forecast_arima(model_fit, steps):
    forecast = model_fit.forecast(steps=steps)
    return forecast
