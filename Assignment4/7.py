def extract_digit_words(input_string):
  
    words = input_string.split()
    

    digit_words = [word for word in words if word.isdigit()]
    
  
    print(digit_words)


if __name__ == "__main__":

    user_input = input("Enter a sequence of words separated by whitespace: ")
    
   
    extract_digit_words(user_input)
