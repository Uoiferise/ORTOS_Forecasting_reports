from forecasting.forecast import Forecast


class Nomenclature:
    """A class designed to aggregate all information for a specific nomenclature"""

    def __init__(self, name: str, data):
        self.__name = name

        self.__historical_data = data.get_historical_data(self.__name)
        self.__current_stock = data.get_current_balances_stock_data(self.__name)
        self.__get_current_orders = []

        # making forecast for this nomenclature
        forecast = Forecast(self)
        forecast.make_forecast()    # creating new attributes

    def get_historical_data(self):
        return self.__historical_data

    def get_current_stock(self):
        return self.__current_stock

    def get_current_orders(self):
        return self.__get_current_orders
