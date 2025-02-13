def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1
try:
    print(factorial(-1))  # Raises ValueError
except ValueError as e:
    print(e) # Output: Factorial is not defined for negative numbers.