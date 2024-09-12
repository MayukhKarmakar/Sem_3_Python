def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == s[::-1]

def ends_with(s, substring):
    return s.endswith(substring)

def capitalize_first_letter_of_each_word(s):
    return ' '.join(word.capitalize() for word in s.split())

def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

def remove_vowels(s):
    vowels = 'aeiouAEIOU'
    return ''.join(char for char in s if char not in vowels)

def longest_word_length(sentence):
    words = sentence.split()
    return max(len(word) for word in words) if words else 0

# Example usage
if __name__ == "__main__":
    input_string = input("Enter a string: ")

    # Reverse the string
    print("Reversed String:", reverse_string(input_string))
    
    # Check if it's a palindrome
    print("Is Palindrome:", is_palindrome(input_string))
    
    # Check if it ends with a specific substring
    substring = input("Enter a substring to check if the string ends with it: ")
    print("Ends with Substring:", ends_with(input_string, substring))
    
    # Capitalize the first letter of each word
    print("Capitalized String:", capitalize_first_letter_of_each_word(input_string))
    
    # Check if it's an anagram of another string
    anagram_string = input("Enter another string to check for anagram: ")
    print("Are Anagrams:", are_anagrams(input_string, anagram_string))
    
    # Remove vowels from the string
    print("String without Vowels:", remove_vowels(input_string))
    
    # Find the length of the longest word in a sentence
    sentence = input("Enter a sentence to find the length of the longest word: ")
    print("Length of Longest Word:", longest_word_length(sentence))
