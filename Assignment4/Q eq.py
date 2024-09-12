import math

def _solve_quadratic_eqn(a, b, c):
    # Calculate discriminant
    discriminant = b**2 - 4*a*c
    
    # Check if roots are real or imaginary
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"Real and distinct roots: {root1} and {root2}"
    elif discriminant == 0:
        root = -b / (2*a)
        return f"Real and equal root: {root}"
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        return f"Complex roots: {real_part} ± {imaginary_part}i"

# Example usage
a = 1
b = -3
c = 2

result = _solve_quadratic_eqn(a, b, c)
print(result)