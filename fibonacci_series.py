def fibonacci_series(n):
    if n == 0 or n == 1 or n == 2:
        return 1
    else:
        return fibonacci_series(n - 1) + fibonacci_series(n - 2)
