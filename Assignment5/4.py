
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}


union_AB = A.union(B)
print("Union of A and B:", union_AB)


intersection_AB = A.intersection(B)
print("Intersection of A and B:", intersection_AB)


is_subset = A.issubset(B)
print("Is A a subset of B?", is_subset)


are_disjoint = A.isdisjoint(B)
print("Are A and B disjoint sets?", are_disjoint)


union_AB_BA = A.union(B).union(B.union(A))
print("Union of A with B and B with A:", union_AB_BA)


symmetric_difference_AB = A.symmetric_difference(B)
print("Symmetric Difference between A and B:", symmetric_difference_AB)


del A
del B
print("Sets A and B have been deleted.")
