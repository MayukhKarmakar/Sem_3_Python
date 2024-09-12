
fruits = ('apple', 'banana', 'cherry')
vegetables = ('carrot', 'broccoli', 'spinach')
animal_products = ('milk', 'cheese', 'eggs')


food_stuff_tp = fruits + vegetables + animal_products
print("Food Stuff Tuple:", food_stuff_tp)


food_stuff_lt = list(food_stuff_tp)
print("Food Stuff List:", food_stuff_lt)


n = len(food_stuff_lt)
if n % 2 == 1:
    middle_item = food_stuff_lt[n // 2]
    middle_slice = [middle_item]
else:
    middle_slice = food_stuff_lt[(n // 2 - 1):(n // 2 + 1)]

print("Middle Item(s):", middle_slice)


first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]

print("First Three Items:", first_three_items)
print("Last Three Items:", last_three_items)


del food_stuff_tp
print("food_stuff_tp has been deleted.")
