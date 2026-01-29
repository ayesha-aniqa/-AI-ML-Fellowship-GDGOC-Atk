def get_factorial(n):
    #Returns factorial
    if n == 0 or n == 1:
        return 1
    return n * get_factorial(n - 1)