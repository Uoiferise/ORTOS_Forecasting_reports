import datetime as dt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from settings import *


class Forecast:
    """Description will be later ... maybe"""

    __DELIVERY_TIME = DELIVERY_TIME
    __NECESSARY_STOCK = NECESSARY_STOCK
    __FORECASTING_PERIOD = FORECASTING_PERIOD
    __MINIMAL_STOCK_FOR_COST = MINIMAL_STOCK_FOR_COST
    __MINIMAL_R2_SCORE_FOR_COSTS = MINIMAL_R2_SCORE_FOR_COSTS
    __MINIMAL_R2_SCORE_FOR_SALES = MINIMAL_R2_SCORE_FOR_SALES

    def __init__(self, nomenclature):
        self.nomenclature = nomenclature

    def get_linear_equation_info(self) -> dict:
        x = self.nomenclature.get_historical_data()
        y = self.nomenclature.get_historical_data()
        regression_model = LinearRegression()    # model initialization
        regression_model.fit(x, y)    # fit the data(train the model)
        y_predicted = regression_model.predict(x)    # predict

        result = {
            'a': regression_model.coef_[0][0],
            'b': regression_model.intercept_[0],
            'rmse': mean_squared_error(y, y_predicted),   # Root mean squared error of the model
            'r2_score': r2_score(y, y_predicted),
            'len_y': len(y)
        }
        return result

    def make_forecast(self):
        # linear_equation_info = self.get_linear_equation_info()

        forecasting_costs = []
        forecasting_sales = []
        forecasting_stocks = []

        self.nomenclature.set_forecasting_costs(forecasting_costs)
        self.nomenclature.set_forecasting_sales(forecasting_sales)
        self.nomenclature.set_forecasting_stocks(forecasting_stocks)
