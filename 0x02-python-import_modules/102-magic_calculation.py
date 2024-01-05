#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        rsl = add(a, b)
        for i in range(4, 6):
            rsl = add(rsl, i)
        return (rsl)
    else:
        return(sub(a, b))
