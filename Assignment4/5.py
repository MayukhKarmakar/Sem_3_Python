
input_sentence = input("Enter a sentence: ")


letters_count = 0
digits_count = 0


for char in input_sentence:
    if char.isalpha():
        letters_count += 1
    elif char.isdigit():
        digits_count += 1


print(f"LETTERS {letters_count}")
print(f"DIGITS {digits_count}")
