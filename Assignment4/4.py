

input_words = input("Enter a sequence of whitespace-separated words: ")


words_list = input_words.split()


unique_sorted_words = sorted(set(words_list))


output_words = ' '.join(unique_sorted_words)


print(output_words)
