# Function to find numbers divisible by 7 but not multiples of 5
def find_special_numbers(start, end):
    special_numbers = []
    for num in range(start, end + 1):
        if num % 7 == 0 and num % 5 != 0:
            special_numbers.append(num)
    return special_numbers


start = 1000
end = 2000


special_numbers = find_special_numbers(start, end)


print(f"Numbers between {start} and {end} that are divisible by 7 but not multiples of 5 are: {special_numbers}")
