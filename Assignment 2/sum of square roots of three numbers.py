import math

def sum_of_square_roots(num1, num2, num3):
    return math.sqrt(num1) + math.sqrt(num2) + math.sqrt(num3)


number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))


result = sum_of_square_roots(number1, number2, number3)

print(f"The sum of the square roots of {number1}, {number2}, and {number3} is {result:.2f}")
