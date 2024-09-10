def series_sum(n):
    sum = 0.0
    for i in range(1, n + 1):
        if i % 2 == 0:
            sum -= 1 / i  # Subtract for even terms
        else:
            sum += 1 / i  # Add for odd terms
    return sum

# Input from the user
n = int(input("Enter a positive integer (n): "))

# Calculate and display the sum
result = series_sum(n)
print(f"The sum of the series up to {n} terms is: {result}")
