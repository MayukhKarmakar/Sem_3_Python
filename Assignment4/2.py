
input_words = input("Enter a comma-separated sequence of words: ")


words_list = input_words.split(',')


words_list.sort()


sorted_words = ','.join(words_list)


print("Sorted words:", sorted_words)
