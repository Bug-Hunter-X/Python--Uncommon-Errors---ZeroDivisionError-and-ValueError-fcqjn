import sys
def function_with_error_handling(x):
    try:
        if x == 0:
            return 1/x
        elif x < 0:
            return x**0.5
        else:
            return x + 1
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!", file=sys.stderr)
        return float('inf') # Or another appropriate return value
    except ValueError:
        print("Error: Cannot compute square root of a negative number!", file=sys.stderr)
        return float('nan') # Or another appropriate return value

result = function_with_error_handling(-5) 
print(result)
result = function_with_error_handling(0)
print(result)
result = function_with_error_handling(5)
print(result)