
def geometric_sequence(start, ratio, terms):
    sequence = []
    current_term = start
    for _ in range(terms):
        sequence.append(current_term)
        current_term *= ratio
    return sequence


start = 2
ratio = 3
terms = 6


sequence = geometric_sequence(start, ratio, terms)


print("The first 6 terms of the geometric sequence are:", sequence)
