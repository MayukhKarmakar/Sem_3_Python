
def fibonacci_series(n):
    fib_series = []
    a, b = 0, 1
    while a <= n:
        fib_series.append(a)
        a, b = b, a + b
    return fib_series


n = int(input("Enter the upper limit for the Fibonacci series: "))


fib_series = fibonacci_series(n)


print(f"Fibonacci series up to {n} is: {fib_series}")
