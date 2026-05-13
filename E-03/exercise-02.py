from math import pi


def square(a):
    print(f"The perimetre of square is:{a * 4}")
    print(f"The area of square is:{a * a}")


def rectangle(a, b):
    print(f"The perimetre of rectangle is:{2 * (a + b)}")
    print(f"The area of rectangle is:{a * b}")


def triangle(*args):
    if len(args) == 3:
        print(f"The perimetre of triangle is:{sum(args)}")
    elif len(args) == 2:
        b = args[0]
        h = args[1]
        print(f"The area of triangle is:{b * h / 2}")


def circle(r):
    print(f"The perimetre of circle is:{2 * pi * r}")
    print(f"The area of circle is:{pi * (r ** 2)}")


choice = -1

while choice != 0:

    choice = int(input(
        "Choose a shape:\n 1) Square\n 2) Rectangle\n 3) Triangle\n 4)  Circle\n 0) Exit\n Enter your choice (0-4)"))

    if choice == 1:
        a = int(input("Please enter the side length of the square:"))
        square(a)

    elif choice == 2:
        b = int(input("Please enter the width of the rectangle:"))
        c = int(input("Please enter the height of the rectangle:"))
        rectangle(b, c)

    elif choice == 3:
        d = input("Enter 3 numbers for perimeter (3 4 5) or 2 numbers for area: ").split()
        values_list = []
        for x in d:
            x = int(x)
            values_list.append(x)

        values = tuple(values_list)
        triangle(*values)

    elif choice == 4:
        e = int(input("Please enter the radius of the circle:"))
        circle(e)

    elif choice == 0:
        print("Good bye 👋🔚")