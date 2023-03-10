# project settings
FOLDER_PATH = 'input_data/input_data.xlsx'

# for class Forecast
DELIVERY_TIME = 3   # months
NECESSARY_STOCK = 9   # months
FORECASTING_PERIOD = DELIVERY_TIME + NECESSARY_STOCK
MINIMAL_STOCK_FOR_COST = 5    # months
AVERAGING_PERIOD = 9    # months
MINIMAL_R2_SCORE_FOR_COSTS = 0.95    # 0 <= R2 <= 1
MINIMAL_R2_SCORE_FOR_SALES = 0.95    # 0 <= R2 <= 1
