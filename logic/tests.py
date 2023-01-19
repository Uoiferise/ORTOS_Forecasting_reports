from settings import *
from get_data import Data
import pandas as pd
from data import *
import os


# os.chdir('/Users/kalyukov.ns/Documents/Python projects/ORTOS_Forecasting_reports')

def data_test():
    data = Data(FOLDER_PATH)
    if isinstance(data.get_nomenclatures(), dict) is not True:
        raise ValueError('method "get_nomenclatures" must return a dict')
    print(data.get_nomenclatures()['Диск ZrO2 Multilayer 3D PRO A3 22 мм Aidite'].get_current_stock())
    print(data.get_nomenclatures()['Диск ZrO2 Multilayer 3D PRO A3 22 мм Aidite'].__dict__)


def run_test():
    data_test()
