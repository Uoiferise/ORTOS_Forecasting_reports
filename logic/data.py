import pandas as pd
import datetime as dt
from nomenclature import Nomenclature


class Data:
    """A class designed to read and process input data"""

    @staticmethod
    def read_historical_data(source: str):
        historical_data = pd.read_excel(
            source,
            sheet_name='historical_data')  # Historical cost and sales data
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

    # @staticmethod
    # def read_current_orders_data(source: str):
    #     current_orders = pd.read_excel(
    #         source,
    #         sheet_name='current_orders')  # Information about current orders
    #     order_numbers = list(int(i) for i in current_orders['ЗП'].unique())
    #     nomenclature_name = current_orders['Номенклатура'].unique()
    #     current_orders_dict = {}
    #     for name in nomenclature_name:
    #         result = {}
    #         df = current_orders.loc[current_orders['Номенклатура'] == name][['ЗП', 'Зак. ост.']]
    #         for order in order_numbers:
    #             result[order] = df.loc[df['ЗП'] == order]['Зак. ост.'].sum()
    #
    #         current_orders_dict[name] = result
    #
    #     order_numbers_dict = {}
    #     for order in order_numbers:
    #         d = str(current_orders.loc[current_orders['ЗП'] == order]['Пост план'].values[0])
    #         if d == 'nan' or d == 'NaT' or d == '(пусто)':
    #             order_numbers_dict[order] = dt.date(2122,
    #                                                 12,
    #                                                 31)
    #         else:
    #             order_numbers_dict[order] = dt.date(int(d.split('-')[0]),
    #                                                 int(d.split('-')[1]),
    #                                                 int(d.split('-')[2][:2]))
    #
    #     sorted_tuples = sorted(order_numbers_dict.items(), key=lambda item: item[1])
    #     sorted_order_numbers_dict = {k: v for k, v in sorted_tuples}
    #     return sorted_order_numbers_dict

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

        # preparing costs data
        df_costs = self.__historical_data[self.__historical_data.Nomenclature_name == nomenclature_name]['Собст расход']
        df_costs.reset_index(drop=True, inplace=True)
        result['costs'] = [float(item) for item in df_costs.values]

        # preparing sales data
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
