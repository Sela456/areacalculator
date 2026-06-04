print("Enter shape whose area is to be calculated: circle, square, rectangle, triangle")
shape = str(input("enter shape: "))


if shape == "circle":
    radius = float(input("enter radius of circle: "))
    area = 3.14 * radius ** 2    
    print("area of circle is: ", round(area,2))


elif shape ==  "square":
    length = int(input("enter length of square: "))
    area = length * length
    print("area of square is :", area)

elif shape == "rectangle":
    length = int(input("enter length of rectangle: "))
    breath = int(input("enter breath of rectangle: "))
    area = length * breath
    print("area of rectangle is: ", area)

elif shape == "triangle":
    length = int(input("enter length of triangle: "))
    breath = int(input("enter breath of triangle: "))
    area = 0.5 * length* breath
    print("area of triangle is: ", area)
    
 