
def print_multiplication_table(num):
    print(f"Multiplication table for {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")


number = int(input("Enter a number: "))


print_multiplication_table(number)
