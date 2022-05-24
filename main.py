import matplotlib.pyplot as plt
import numpy as np

from data_io import *
from methods.lagrange import lagranz
from methods.nuthon import table as tb, get_corner, newton

if __name__ == '__main__':
    input_type = ask_input_type()

    if input_type == 2:
        func = chose_func()
        table = NumTable()
        argument = get_argument()
        table.from_void(argument, func)
        x = np.array(table.x_arr, dtype=float)
        y = np.array(table.y_arr, dtype=float)

    else:
        table = input_num_table()
        argument = get_argument()
        x = np.array(table.x_arr, dtype=float)
        y = np.array(table.y_arr, dtype=float)

    middle = tb(x, y)

    n = get_corner(middle)
    newton = newton(n, argument, x)
    print(lagranz(x, y, argument))
    print("Интерполяция Ньютона: {}".format(newton))
    xnew = np.linspace(np.min(x), np.max(x), 100)
    ynew = [lagranz(x, y, i) for i in xnew]
    plt.plot(x, y, "r", )
    plt.plot(x, y, 'o', xnew, ynew)
    plt.scatter(argument, newton, color="purple")
    plt.scatter(argument, lagranz(x, y, argument), color="purple")
    plt.grid(True)
    plt.show()
