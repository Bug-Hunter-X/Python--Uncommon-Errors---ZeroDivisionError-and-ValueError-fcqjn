def function_with_uncommon_error(x):
    if x == 0:
        return 1/x  # ZeroDivisionError
    elif x < 0:
        return x**0.5 # ValueError if x is negative
    else:
        return x + 1

result = function_with_uncommon_error(-5)