
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def is_krishnamurthy_number(num):
  
    digits = str(num)
    sum_of_factorials = 0
    
    
    for digit in digits:
        sum_of_factorials += factorial(int(digit))
    
    
    return sum_of_factorials == num


number = 145
if is_krishnamurthy_number(number):
    print(f"{number} is a Krishnamurthy number.")
else:
    print(f"{number} is not a Krishnamurthy number.")
