# pyinfix (Infixes for Python)

## Why?

No practical reason, just for fun. The "readability" achieved using this is not worth the performance tradeoff. There are many interesting Python features used here, so I hope you can learn something.
Have fun! ^^

## Examples

```py
from main import Infix

add = Infix(lambda x, y: x+y)
print(2 @ add @ 2)

subtract = Infix(lambda x, y: x-y)
print(4 >> subtract << 2)
```

You can even mix them:

```py
print(2 | add ^ 1)
```

Find supported ones in the [source file](./main.py) in *COVERED* variable.
Why is power not supported (**)? Because Python executes operations with it in a different order, that would require writing less cool code.
