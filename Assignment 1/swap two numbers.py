
def swap_numbers(a, b):
    a, b = b, a
    return a, b
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num1, num2 = swap_numbers(num1, num2)
print(f"After swapping: first number = {num1}, second number = {num2}")
