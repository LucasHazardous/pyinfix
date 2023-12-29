from main import Infix

FIRST = 3
SECOND = 2
assert(type(FIRST) == type(SECOND))

for operation in Infix.COVERED:
    if not hasattr(type(FIRST), f"__{operation}__"): continue
    infix = Infix(func := eval(f"lambda x, y: (x).__{operation}__(y)"))
    for infix_operation in Infix.COVERED:
        assert(getattr(getattr(infix, f"__r{infix_operation}__")(FIRST), f"__{infix_operation}__")(SECOND) == func(FIRST, SECOND))

print("All tests passed successfully!")
