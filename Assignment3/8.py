import math

def factorial(num):
    """Helper function to compute the factorial of a number"""
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

def cosine_series(x, n):
    """Function to compute cos(x) using the series expansion up to n terms"""
    cos_sum = 0.0
    
    for i in range(n):
        # Compute each term in the series: x^(2*i) / (2*i)!
        term = ((-1)**i) * (x**(2*i)) / factorial(2*i)
        cos_sum += term
        
    return cos_sum

# Input from the user
x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms (n): "))

# Compute cos(x) using the series
result = cosine_series(x, n)

# Display the result
print(f"cos({x}) using {n} terms is: {result}")
