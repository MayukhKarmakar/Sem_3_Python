
def is_armstrong_number(num):
    num_str = str(num)
    num_of_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_of_digits for digit in num_str)
    return sum_of_powers == num


number = int(input("Enter a number to check if it is an Armstrong number: "))

if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
