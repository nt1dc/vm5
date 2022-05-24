class NumTable:
    def __init__(self):
        self.table = []
        self.x_arr = []
        self.y_arr = []

    def add_pair(self, x, y):
        self.x_arr.append(x)
        self.y_arr.append(y)
        self.table.append(Pair(x, y))

    def from_void(self, argument, func):
        self.add_pair(argument - 1, func.func_format(argument - 1))
        self.add_pair(argument + 1, func.func_format(argument + 1))
        self.add_pair(argument + 2, func.func_format(argument + 2))


class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
