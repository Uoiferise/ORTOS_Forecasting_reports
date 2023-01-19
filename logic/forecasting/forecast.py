from forecasting.analysis import get_linear_regression_info
from settings import *


class Forecast:
    """A class designed to predict purchases for a specific nomenclature"""

    __DELIVERY_TIME = DELIVERY_TIME
    __NECESSARY_STOCK = NECESSARY_STOCK
    __FORECASTING_PERIOD = FORECASTING_PERIOD
    __MINIMAL_STOCK_FOR_COST = MINIMAL_STOCK_FOR_COST
    __MINIMAL_R2_SCORE_FOR_COSTS = MINIMAL_R2_SCORE_FOR_COSTS
    __MINIMAL_R2_SCORE_FOR_SALES = MINIMAL_R2_SCORE_FOR_SALES

    def __init__(self, nomenclature):
        self.nomenclature = nomenclature

    def set_linear_regression_info(self):
        x = self.nomenclature.get_historical_data()['costs']
        y = self.nomenclature.get_historical_data()['costs']
        self.nomenclature.linear_regression_info = get_linear_regression_info(x, y)

    def get_forecasting_method(self):
        pass

    def make_forecast(self):
        self.set_linear_regression_info()


        forecasting_costs = []
        forecasting_sales = []
        forecasting_stocks = []

        self.nomenclature.forecasting_costs = forecasting_costs
        self.nomenclature.forecasting_sales = forecasting_sales
        self.nomenclature.forecasting_stocks = forecasting_stocks
