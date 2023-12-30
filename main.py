class Infix:
    COVERED = ["or", "add", "sub", "mul", 
    "matmul", "truediv", "floordiv", "mod", 
    "lshift", "rshift", "and", "xor"]
    INITIALIZED = False
    def __init__(self, func):
        self.func = func
        if(not Infix.INITIALIZED):
            Infix.INITIALIZED = True
            exec("".join(f"""
def __r{operation}__(self, other):
    return Infix(lambda var: self.func(other, var))
def __{operation}__(self, other):
    return self.func(other)
            """ for operation in Infix.COVERED), globals(), method_dict := {})
            [setattr(self.__class__, method_name, method) for method_name, method in method_dict.items()]
