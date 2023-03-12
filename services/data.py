import pandas as pd
import datetime as dt
from nomenclature import Nomenclature


class Data:
    """A class designed to read and process input input_data"""

    @staticmethod
    def read_historical_data(source: str):
        historical_data = pd.read_excel(
            source,
            sheet_name='historical_data')  # Historical cost and sales input_data
        historical_data.rename(columns={'Номенклатура': 'Nomenclature_name'}, inplace=True)
        print('read_historical_data_done')
        return historical_data

    @staticmethod
    def read_current_balances_data(source: str):
        current_balances_data = pd.read_excel(
            source,
            sheet_name='current_balances')  # Information from the inventory and orders report
        current_balances_data.rename(columns={'Номенклатура': 'Nomenclature_name'}, inplace=True)
        print('read_current_balances_data_done')
        return current_balances_data

    def __init__(self, source: str):
        self.__source = source
        self.__historical_data = self.read_historical_data(self.__source)
        self.__current_balances_data = self.read_current_balances_data(self.__source)
        # self.__current_orders_data = self.read_current_orders_data(self.__source)

        nomenclatures_dict = {}
        for nomenclature_name in self.__current_balances_data['Nomenclature_name'].unique():
            nomenclatures_dict[nomenclature_name] = Nomenclature(name=nomenclature_name, data=self)

        self.__nomenclatures = nomenclatures_dict

    def get_historical_data(self, nomenclature_name) -> dict:
        result = dict()

        # preparing costs input_data
        df_costs = self.__historical_data[self.__historical_data.Nomenclature_name == nomenclature_name]['Собст расход']
        df_costs.reset_index(drop=True, inplace=True)
        result['costs'] = [float(item) for item in df_costs.values]

        # preparing sales input_data
        df_sales = self.__historical_data[self.__historical_data.Nomenclature_name == nomenclature_name]['Продажи']
        df_sales.reset_index(drop=True, inplace=True)
        result['sales'] = [float(item) for item in df_sales.values]
        return result

    def get_current_balances_stock_data(self, nomenclature_name) -> float:
        current_stock = float(self.__current_balances_data[self.__current_balances_data.Nomenclature_name == nomenclature_name]['Св ост'].values[0])
        return current_stock

    # def get_current_orders_data(self, nomenclature_name):
    #     return self.__current_orders_data

    def get_nomenclatures(self) -> dict:
        return self.__nomenclatures
