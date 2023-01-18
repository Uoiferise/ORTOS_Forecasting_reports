class Nomenclature:
    """Description will be later ... maybe"""

    __NOMENCLATURES = {}

    @classmethod
    def get_all_nomenclatures(cls):
        return cls.__NOMENCLATURES

    def __init__(self, name: str, historical_data: list):
        self.__name = name
        self.__historical_data = historical_data
        self.__NOMENCLATURES[self.__name] = self

        self.__forecasting_method = None
        self.__forecasting_costs = None
        self.__forecasting_sales = None
        self.__forecasting_stocks = None

    def get_historical_data(self, period):
        return self.__historical_data[-period::]

    def set_forecasting_method(self):
        self.__forecasting_method = 'LR'

    def set_forecasting_costs(self, forecasting_costs: list):
        self.__forecasting_costs = forecasting_costs

    def set_forecasting_sales(self, forecasting_sales: list):
        self.__forecasting_costs = forecasting_sales

    def set_forecasting_stocks(self, forecasting_stocks: list):
        self.__forecasting_costs = forecasting_stocks
