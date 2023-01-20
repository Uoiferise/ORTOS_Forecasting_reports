def liner_regression_forecasting(liner_reg_info, data, forecasting_period, mean_period):
    result = []
    for i in range(1, forecasting_period + 1):
        a = liner_reg_info['a']
        b = liner_reg_info['b']
        x = liner_reg_info['len_y'] + i
        y = a * x + b  # predicted mean cost
        predicted_cost = (y * mean_period) - sum(data[-1 * mean_period + 1:])
        if predicted_cost < 0:
            predicted_cost = 0

        result.append(predicted_cost)
    return result


def mean_score_forecasting(data, forecasting_period, period_for_mean_cost):
    result = []
    for _ in range(forecasting_period):
        period_for_mean_cost = 3
        try:
            mean_cost = sum(data[-period_for_mean_cost:]) / len(data[-period_for_mean_cost:])  # last n month
        except ZeroDivisionError:
            mean_cost = 0
        predicted_cost = mean_cost * 1.3  # mean cost * coefficient
        result[0].append(round(predicted_cost, 2))
    return result


def cost_forecasting(liner_reg_info, data, forecasting_period, mean_period):
    if liner_reg_info['method'] == 'LR':
        liner_regression_forecasting(liner_reg_info, data, forecasting_period, mean_period)
    elif liner_reg_info['method'] == 'LR':
        mean_score_forecasting(data, forecasting_period, mean_period)
