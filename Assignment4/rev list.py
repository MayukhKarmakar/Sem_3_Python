def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr


example_array = [1, 2, 3, 4, 5]
reversed_array = reverse_list(example_array)
print(reversed_array)