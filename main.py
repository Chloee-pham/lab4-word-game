# Word Game - Lab 4

def fibonacci(n):
    """
    Recursive Fibonacci function.
    Returns the nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    pass

if __name__ == "__main__":
    main()
