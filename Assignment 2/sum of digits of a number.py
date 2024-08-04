
def sum_of_digits(num):
    
    sum_digits = 0
    
    
    while num > 0:
        
        sum_digits += num % 10
       
        num = num // 10
    
    return sum_digits


number = 12345
result = sum_of_digits(number)


print(f"The sum of the digits of {number} is: {result}")
