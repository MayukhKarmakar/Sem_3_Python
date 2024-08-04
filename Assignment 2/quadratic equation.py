import math


def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
       
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return (root1, root2)
    elif discriminant == 0:
       
        root = -b / (2 * a)
        return (root,)
    else:
      
        realPart = -b / (2 * a)
        imaginaryPart = math.sqrt(-discriminant) / (2 * a)
        return (realPart + imaginaryPart * 1j, realPart - imaginaryPart * 1j)


a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))


roots = solve_quadratic(a, b, c)


if len(roots) == 2:
    print(f"The roots of the equation are {roots[0]} and {roots[1]}.")
elif len(roots) == 1:
    print(f"The root of the equation is {roots[0]}.")
else:
    print(f"The roots of the equation are {roots[0]} and {roots[1]}.")
