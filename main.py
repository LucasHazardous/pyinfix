class Infix:
    COVERED = ["or", "add", "sub", "mul", 
    "matmul", "truediv", "floordiv", "mod", 
    "lshift", "rshift", "and", "xor"]
    def __init__(self, func):
        self.func = func
        exec("".join(f"""
def __r{operation}__(self, other):
    return Infix(lambda var: self.func(other, var))
def __{operation}__(self, other):
    return self.func(other)
        """ for operation in Infix.COVERED), globals(), method_dict := {})
        [setattr(self.__class__, method, method_dict[method]) for method in method_dict]
