
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def factorial_series(n):
    series = []
    for i in range(1, n + 1):
        series.append(factorial(i))
    return series


N = int(input("Enter the number of terms: "))


series = factorial_series(N)


print(f"The series up to {N} terms is:", series)
