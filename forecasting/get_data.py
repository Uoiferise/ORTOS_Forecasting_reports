import pandas as pd
import datetime as dt


class Data:
    """Description will be later ... maybe"""

    @staticmethod
    def read_historical_data(source):
        historical_data = pd.read_excel(
            source,
            sheet_name='historical_data')  # Historical cost and sales data
        historical_data.rename(columns={'Номенклатура': 'nomenclature'}, inplace=True)
        return historical_data

    @staticmethod
    def read_current_balances_data(source):
        current_balances_data = pd.read_excel(
            source,
            sheet_name='current_balances')  # Information from the inventory and orders report
        return current_balances_data

    @staticmethod
    def read_current_orders_data(source):
        current_orders = pd.read_excel(
            source,
            sheet_name='current_orders')  # Information about current orders
        order_numbers = list(int(i) for i in current_orders['ЗП'].unique())
        nomenclature_name = current_orders['Номенклатура'].unique()
        current_orders_dict = {}
        for name in nomenclature_name:
            result = {}
            df = current_orders.loc[current_orders['Номенклатура'] == name][['ЗП', 'Зак. ост.']]
            for order in order_numbers:
                result[order] = df.loc[df['ЗП'] == order]['Зак. ост.'].sum()

            current_orders_dict[name] = result

        order_numbers_dict = {}
        for order in order_numbers:
            d = str(current_orders.loc[current_orders['ЗП'] == order]['Пост план'].values[0])
            if d == 'nan' or d == 'NaT' or d == '(пусто)':
                order_numbers_dict[order] = dt.date(2122,
                                                    12,
                                                    31)
            else:
                order_numbers_dict[order] = dt.date(int(d.split('-')[0]),
                                                    int(d.split('-')[1]),
                                                    int(d.split('-')[2][:2]))

        sorted_tuples = sorted(order_numbers_dict.items(), key=lambda item: item[1])
        sorted_order_numbers_dict = {k: v for k, v in sorted_tuples}
        return sorted_order_numbers_dict

    def __init__(self, source):
        self.__source = source
        self.__historical_data = self.read_historical_data(self.__source)
        self.__current_balances_data = self.read_current_balances_data(self.__source)
        self.__current_orders_data = self.read_current_orders_data(self.__source)
        self.__nomenclatures = self.__current_balances_data['Номенклатура'].unique()

    def get_data(self):
        return self.__historical_data
