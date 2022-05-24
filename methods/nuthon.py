def table(x_, y):
    """
         Получить таблицу интерполяции Ньютона
         : param x_: значение списка x
         : param y: значение списка y
         : return: вернуть таблицу интерполяции
    """
    quotient = [[0] * len(x_) for _ in range(len(x_))]
    for n_ in range(len(x_)):
        quotient[n_][0] = y[n_]
    for i in range(1, len(x_)):
        for j in range(i, len(x_)):
            # j-i определяет диагональные элементы
            quotient[j][i] = (quotient[j][i - 1] - quotient[j - 1][i - 1]) / (x_[j] - x_[j - i])
    return quotient


def get_corner(result):
    """
         Получить диагональные элементы через таблицу интерполяции
         : param result: результат таблицы интерполяции
         : return: диагональный элемент
    """
    link = []
    for i in range(len(result)):
        link.append(result[i][i])
    return link


def newton(data_set, x_p, x_7):
    """
         Результат интерполяции Ньютона
         : param data_set: диагональ решаемой задачи
         : param x_p: входное значение
         : param x_7: исходное значение списка x
         : return: результат интерполяции Ньютона
    """
    result = data_set[0]
    for i in range(1, len(data_set)):
        p = data_set[i]
        for j in range(i):
            p *= (x_p - x_7[j])
        result += p
    return result
