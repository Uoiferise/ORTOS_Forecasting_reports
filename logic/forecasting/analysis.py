from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import datetime
from dateutil.relativedelta import *


def get_linear_regression_info(x, y) -> dict:
    regression_model = LinearRegression()  # model initialization
    regression_model.fit(x, y)  # fit the data(train the model)
    y_predicted = regression_model.predict(x)  # predict

    result = {
        'a': regression_model.coef_[0][0],
        'b': regression_model.intercept_[0],
        'rmse': mean_squared_error(y, y_predicted),  # Root mean squared error of the model
        'r2_score': r2_score(y, y_predicted),
        'len_y': len(y),
    }
    return result


def stock_forecasting(period, delivery_time, cost, sale, stock_0,
                      minimal_cost_stock, order_numbers_dict, current_orders_dict):
    stock = [stock_0]
    color = []
    buy = 0

    date_forecasting = datetime.date.today()

    # cycle for predicting monthly balances
    for i in range(period):
        color.append([])

        date_forecasting = date_forecasting + relativedelta(months=+1)

        # checking balances for minimum stock for in-house production
        if stock[i] <= sum(cost[i:i+minimal_cost_stock]):
            flag = False    # close sales
        else:
            flag = True    # don't close sales

        # selection of orders that will arrive in the forecast month
        orders = []
        for k in order_numbers_dict.keys():
            order_date = order_numbers_dict[k]

            if order_date < datetime.date.today() or current_orders_dict.get(k, 0) == 0:
                continue
            elif order_date < date_forecasting:
                orders.append(k)
            else:
                break

        # forecasting balances depending on the availability of orders and sales
        value = stock[i]
        if len(orders) > 0:    # the period is divided into segments depending on the delivery dates
            start_date = date_forecasting + relativedelta(months=-1)
            end_date = date_forecasting
            delta_all = (end_date - start_date).days

            for index, item in enumerate(orders):
                order_date = order_numbers_dict[item]
                delta_order = (order_date - start_date).days

                coeff_1 = float(delta_order / delta_all)
                start_date = order_date    # for next iteration

                if flag:  # if we don't close sales
                    if value >= cost[i] * coeff_1 + sale[i] * coeff_1:  # don't need a buy
                        value -= cost[i] * coeff_1 + sale[i] * coeff_1
                    else:  # need a buy!
                        buy += cost[i] * coeff_1 + sale[i] * coeff_1 - value
                        value -= cost[i] * coeff_1 + sale[i] * coeff_1
                else:
                    if value >= cost[i] * coeff_1:  # need a buy for sales
                        buy += sale[i] * coeff_1
                        value -= cost[i] * coeff_1
                    else:  # need a buy for sales and costs
                        buy += cost[i] * coeff_1 + sale[i] * coeff_1 - value
                        value -= cost[i] * coeff_1

                if value > 0 and flag:
                    color[i].append('g')
                elif value > 0:
                    color[i].append('y')
                else:
                    color[i].append('r')
                    value = 0.0

                value += current_orders_dict[item]
                current_orders_dict[item] = 0

                if index == len(orders) - 1:
                    delta_end = (end_date - order_date).days
                    coeff_2 = float(delta_end / delta_all)

                    if flag:    # if we don't close sales
                        if value >= cost[i] * coeff_2 + sale[i] * coeff_2:    # don't need a buy
                            value -= cost[i] * coeff_2 + sale[i] * coeff_2
                        else:   # need a buy!
                            buy += cost[i] * coeff_2 + sale[i] * coeff_2 - value
                            value -= cost[i] * coeff_2 + sale[i] * coeff_2
                    else:
                        if value >= cost[i] * coeff_2:    # need a buy for sales
                            buy += sale[i] * coeff_2
                            value -= cost[i] * coeff_2
                        else:    # need a buy for sales and costs
                            buy += cost[i] * coeff_2 + sale[i] * coeff_2 - value
                            value -= cost[i] * coeff_2

                    if value > 0 and flag:
                        color[i].append('g')
                    elif value > 0:
                        color[i].append('y')
                    else:
                        color[i].append('r')
                        value = 0.0
        else:
            if flag:    # if we don't close sales
                if value >= (cost[i] + sale[i]):    # don't need a buy
                    value = value - (cost[i] + sale[i])
                else:    # need a buy!
                    buy += cost[i] + sale[i] - value
                    value = value - (cost[i] + sale[i])
            else:
                if value >= cost[i]:    # need a buy for sales
                    buy += sale[i]
                    value = value - cost[i]
                else:    # need a buy for sales and costs
                    buy += cost[i] + sale[i] - value
                    value = value - cost[i]

            if value > 0 and flag:
                color[i].append('g')
            elif value > 0:
                color[i].append('y')
            else:
                color[i].append('r')
                value = 0.0

        stock.append(float(value))
        color = list(map(lambda x: ''.join(x), color))

        # we don't must buy a nomenclature if we can't to delivery purchase in forecasting period
        if i < delivery_time:
            buy = 0

    return stock[1:], color, float(buy)
