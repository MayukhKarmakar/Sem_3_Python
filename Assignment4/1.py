


input_string = input("Enter a sentence: ")


length_of_string = len(input_string)


substring_found = "country" in input_string


import string
words = input_string.translate(str.maketrans('', '', string.punctuation)).split()
word_count = {}


for word in words:
    word_count[word] = word_count.get(word, 0) + 1


print(f"Length of the string: {length_of_string}")
print(f"Is 'country' found? {substring_found}")
print("Word occurrences:")
for word, count in word_count.items():
    print(f"{word}: {count}")
