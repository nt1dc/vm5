class Function:
    def __init__(self, str_format):
        self.string_format = str_format
        self.func_format = lambda x: eval(self.string_format)

functions = {
    0: "x+1",
}
