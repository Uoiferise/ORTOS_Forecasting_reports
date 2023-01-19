from forecasting import Forecast


class Nomenclature:
    """Description will be later ... maybe"""

    def __init__(self, name: str, data):
        self.__name = name
        self.__historical_data = data.get_historical_data(self.__name)
        self.__current_stock = data.get_current_balances_stock_data(self.__name)

        # making forecast for this nomenclature
        forecast = Forecast(nomenclature=self)
        forecast.make_forecast()

        self.__forecasting_method = None
        self.__forecasting_costs = None
        self.__forecasting_sales = None
        self.__forecasting_stocks = None

    def get_historical_data(self):
        return self.__historical_data

    def get_current_stock(self):
        return self.__current_stock

    def set_forecasting_method(self):
        self.__forecasting_method = 'LR'

    def set_forecasting_costs(self, forecasting_costs: list):
        self.__forecasting_costs = forecasting_costs

    def set_forecasting_sales(self, forecasting_sales: list):
        self.__forecasting_costs = forecasting_sales

    def set_forecasting_stocks(self, forecasting_stocks: list):
        self.__forecasting_costs = forecasting_stocks
