import math

def factorial(num):
    """Helper function to compute the factorial of a number"""
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

def sine_series(x, n):
    """Function to compute sin(x) using the series expansion up to n terms"""
    sine_sum = 0.0
    
    for i in range(n):
      
        term = ((-1)**i) * (x**(2*i + 1)) / factorial(2*i + 1)
        sine_sum += term
        
    return sine_sum


x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms (n): "))


result = sine_series(x, n)


print(f"sin({x}) using {n} terms is: {result}")
