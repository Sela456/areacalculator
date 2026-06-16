# areacircle.py

def circle_area(radius):
    return 3.14 * radius ** 2


def square_area(length):
    return length * length


def rectangle_area(length, breadth):
    return length * breadth


def triangle_area(length, breadth):
    return 0.5 * length * breadth


def main():
    print("Enter shape whose area is to be calculated:"
          " circle, square, rectangle, triangle")
    shape = input("enter shape: ").lower()

    if shape == "circle":
        radius = float(input("enter radius of circle: "))
        print("area of circle is:", round(circle_area(radius), 2))

    elif shape == "square":
        length = float(input("enter length of square: "))
        print("area of square is:", square_area(length))

    elif shape == "rectangle":
        length = float(input("enter length of rectangle: "))
        breadth = float(input("enter breadth of rectangle: "))
        print("area of rectangle is:", rectangle_area(length, breadth))

    elif shape == "triangle":
        length = float(input("enter length of triangle: "))
        breadth = float(input("enter breadth of triangle: "))
        print("area of triangle is:", triangle_area(length, breadth))

    else:
        print("Invalid shape")


if __name__ == "__main__":
    main()
