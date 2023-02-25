import math
# Given 2 sides of a right-angle triangle, find the 3rd
print("""Which sides do you have?
        A) height and base
        B) Height and Hypotenuse
        C) Base and Hypotenuse
""")
choise = input("Choose either A, B and C: ")
if choise.lower() == 'a':
    a, b = input("Enter the base and the height of the triangle: ").split()
    a = int(a)
    b = int(b)
    c = math.sqrt((a*a) + (b*b))
    print(f"The hypotenuse of the triangle is: {c}")
elif choise.lower() == 'b':
    a, c = input("Enter the height and Hypotenuse of the triangle: ").split()
    a = int(a)
    c = int(c)
    b = math.sqrt(((c*c) - (a*a)))
    print(f"The base of the triangle is: {b}")
elif choise.lower() == 'c':
    b, c = input("Enter the base and Hypotenuse of the triangle: ").split()
    b = int(b)
    c = int(c)
    a = math.sqrt(((c*c) - (b*b)))
    print(f"The base of the triangle is: {a}")
