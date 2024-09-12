from collections import Counter

def count_characters(input_string):
    
    char_count = Counter(input_string)
    
   
    for char in sorted(char_count.keys()):
        print(f"{char},{char_count[char]}")


if __name__ == "__main__":
   
    user_input = input("Enter a string: ")
    
    
    count_characters(user_input)
