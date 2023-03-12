from forecasting.liner_regression import get_linear_regression_info, preparing_data
from forecasting.cost_forecasting import cost_forecasting
from settings import *


class Forecast:
    """A class designed to predict purchases for a specific nomenclature"""

    __DELIVERY_TIME = DELIVERY_TIME
    __NECESSARY_STOCK = NECESSARY_STOCK
    __FORECASTING_PERIOD = FORECASTING_PERIOD
    __MINIMAL_STOCK_FOR_COST = MINIMAL_STOCK_FOR_COST
    __AVERAGING_PERIOD = AVERAGING_PERIOD
    __MINIMAL_R2_SCORE_FOR_COSTS = MINIMAL_R2_SCORE_FOR_COSTS
    __MINIMAL_R2_SCORE_FOR_SALES = MINIMAL_R2_SCORE_FOR_SALES

    def __init__(self, nomenclature):
        self.nomenclature = nomenclature

    def set_linear_regression_info(self, analytics_name: str):
        x, y = preparing_data(self.nomenclature.get_historical_data()[analytics_name], self.__AVERAGING_PERIOD)
        self.nomenclature.linear_regression_info[analytics_name] = get_linear_regression_info(x, y)
        self.set_forecasting_method(analytics_name)

    def set_forecasting_method(self, analytics_name: str):
        if analytics_name == 'costs':
            const = self.__MINIMAL_R2_SCORE_FOR_COSTS
        elif analytics_name == 'sales':
            const = self.__MINIMAL_R2_SCORE_FOR_SALES
        else:
            const = 0

        if self.nomenclature.linear_regression_info[analytics_name]['r2_score'] >= const:
            self.nomenclature.linear_regression_info[analytics_name]['method'] = 'LR'
        else:
            self.nomenclature.linear_regression_info[analytics_name]['method'] = 'MS'

    def make_forecast(self):
        self.set_linear_regression_info('costs')
        self.set_linear_regression_info('sales')

        forecasting_costs = cost_forecasting(liner_reg_info=self.nomenclature.linear_regression_info['costs']['method'],
                                             data=None,
                                             forecasting_period=None,
                                             mean_period=self.__AVERAGING_PERIOD)
        forecasting_sales = cost_forecasting(self.nomenclature.lis)
        forecasting_stocks = []

        self.nomenclature.forecasting_costs = forecasting_costs
        self.nomenclature.forecasting_sales = forecasting_sales
        self.nomenclature.forecasting_stocks = forecasting_stocks
