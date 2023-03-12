from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np


def preparing_data(data: list, averaging_period: int) -> tuple:
    y = np.array([
        [sum(data[i:i + averaging_period]) / averaging_period] for i in range(len(data) - averaging_period + 1)
    ])
    x = np.array([[i] for i in range(1, len(y) + 1)])
    return x, y


def get_linear_regression_info(x, y) -> dict:
    result = {
        'a': None,
        'b': None,
        'rmse': None,  # Root mean squared error of the model
        'r2_score': None,
        'len_y': None,
    }
    if len(x) > 10:
        regression_model = LinearRegression()  # model initialization
        regression_model.fit(x, y)  # fit the input_data(train the model)
        y_predicted = regression_model.predict(x)  # predict

        result = {
            'a': regression_model.coef_[0][0],
            'b': regression_model.intercept_[0],
            'rmse': mean_squared_error(y, y_predicted),  # Root mean squared error of the model
            'r2_score': r2_score(y, y_predicted),
            'len_y': len(y),
        }
    return result
