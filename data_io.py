from func_class import *
from num_table import NumTable


def ask_input_type():
    type = 0
    while type != 1 and type != 2:
        try:
            type = int(input("Введите 1, чтобы ввести с клавиатуры 2, чтобы взять готовую функцию "))
        except ValueError:
            print("Введите 1 или 2")
    return type


def chose_func():
    functions_nums = []
    for i in range(len(functions)):
        functions_nums.append(i)
        print(f"{i} : {functions[i]}")
    fun_num = -1

    while fun_num not in functions_nums:
        try:
            print("выберете номер функции")
            fun_num = int(input())
        except:
            Exception
    return Function(functions[fun_num])


def input_num_table():
    table = NumTable()
    print("введите колличество строк в таблице ")
    n = int(input())
    for i in range(n):
        print("Введите точки через пробел: ")
        try:
            temp_list = list(map(float, input().strip().split()))
            if len(temp_list) != 2:
                raise ValueError
            table.add_pair(temp_list[0], temp_list[1])

        except ValueError:
            print("Неправильный формат ввода")
            exit()
    return table


def get_argument():
    print("введите аргумент")
    argument = float(input())
    return argument
