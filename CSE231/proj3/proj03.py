import math
BANNER = '''

╭━━━━╮╱╱╱╱╱╱╱╱╱╱╭╮
┃╭╮╭╮┃╱╱╱╱╱╱╱╱╱╱┃┃
╰╯┃┃┣┻┳┳━━┳━╮╭━━┫┃╭━━╮
╱╱┃┃┃╭╋┫╭╮┃╭╮┫╭╮┃┃┃┃━┫
╱╱┃┃┃┃┃┃╭╮┃┃┃┃╰╯┃╰┫┃━┫
╱╱╰╯╰╯╰┻╯╰┻╯╰┻━╮┣━┻━━╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯
'''
count = 0 #initializing variables to be used later
side_AB_int = 0
side_BC_int = 0
side_CA_int = 0
valid = 0
tri_type = 0
s_int = 0
angle_a_int = 0
angle_b_int = 0
angle_c_int = 0
print(BANNER)
print()
cont = input("Do you wish to process a triangle (Y or N)?  ").lower() #initial ask of continue y/n
while cont == "y":
    side_AB_int = int(input("Enter length of side AB: ")) + .0001 # adds trivial amount so output includes .0
    print()
    side_BC_int = int(input("Enter length of side BC: ")) + .0001
    print()
    side_CA_int = int(input("Enter length of side CA: ")) + .0001
    print()
    print()
    if side_AB_int + side_BC_int == side_CA_int or side_AB_int + side_CA_int == side_BC_int or side_BC_int + side_CA_int == side_AB_int: #test for degen triangle
        print("Degenerate Triangle")
        print()
    elif side_AB_int + side_BC_int < side_CA_int or side_AB_int + side_CA_int < side_BC_int or side_BC_int + side_CA_int < side_AB_int: #test for not a triangle
        print("Not A Triangle")
        print()
    else: #we now know it is a valid triangle
        count = count + 1 #adds to count of valid triangles
        print("Valid Triangle")
        print()
        print("Triangle sides:")
        print("Length of side AB: " + str(round(side_AB_int,1))) #displays lengths of triangles
        print("Length of side BC: " + str(round(side_BC_int,1)))
        print("Length of side CA: " + str(round(side_CA_int,1)))
        print()
        print("Degree measure of interior angles:")
        print("Angle A: " + str(round((180/math.pi)*(math.acos(((side_CA_int**2)+(side_AB_int**2)-(side_BC_int**2))/(2*side_CA_int*side_AB_int))),1)))
        angle_a_int = (180/math.pi)*(math.acos(((side_CA_int**2)+(side_AB_int**2)-(side_BC_int**2))/(2*side_CA_int*side_AB_int))) #calculates interior angles in degrees
        print("Angle B: " + str(round((180/math.pi)*(math.acos(((side_BC_int**2)+(side_AB_int**2)-(side_CA_int**2))/(2*side_BC_int*side_AB_int))),1)))
        angle_b_int = (180/math.pi)*(math.acos(((side_BC_int**2)+(side_AB_int**2)-(side_CA_int**2))/(2*side_BC_int*side_AB_int)))
        print("Angle C: " + str(round((180/math.pi)*(math.acos(((side_BC_int**2)+(side_CA_int**2)-(side_AB_int**2))/(2*side_BC_int*side_CA_int))),1)))
        angle_c_int = (180/math.pi)*(math.acos(((side_BC_int**2)+(side_CA_int**2)-(side_AB_int**2))/(2*side_BC_int*side_CA_int)))
        print()
        print("Radian measure of interior angles")
        print("Angle A: " + str(round((math.acos(((side_CA_int**2)+(side_AB_int**2)-(side_BC_int**2))/(2*side_CA_int*side_AB_int))),1))) #calculates interior angles in radians
        print("Angle B: " + str(round((math.acos(((side_BC_int**2)+(side_AB_int**2)-(side_CA_int**2))/(2*side_BC_int*side_AB_int))),1)))
        print("Angle C: " + str(round((math.acos(((side_BC_int**2)+(side_CA_int**2)-(side_AB_int**2))/(2*side_BC_int*side_CA_int))),1)))
        print()
        print("Perimeter and Area of triangle:")
        print("Perimeter of triangle: " + str(round(side_AB_int + side_BC_int + side_CA_int,1))) #calculates permimeter
        s_int = .5 * (side_AB_int + side_BC_int + side_CA_int) #establishes variable used in next calculation
        print("Area of triangle: " + str(round(((s_int*(s_int-side_AB_int)*(s_int-side_BC_int)*(s_int-side_CA_int))**.5),1))) #calculates area of triangle
        print()
        print("Types of triangle:")
        if side_AB_int == side_BC_int == side_CA_int:
            print("Equilateral Triangle") #tests for equilateral triangle
        if side_AB_int == side_CA_int or side_AB_int == side_BC_int or side_BC_int == side_CA_int:
            print("Isosceles Triangle") #tests for isesceles triangle
        if side_AB_int != side_BC_int != side_CA_int:
            print("Scalene Triangle") #tests for scalene triangle
        if angle_a_int == 90 or angle_b_int == 90 or angle_c_int == 90:
            print("Right Triangle") #tests for right triangle
        if angle_a_int > 90 or angle_b_int > 90 or angle_c_int > 90:
            print("Obtuse Triangle") #tests for obtuse triangle (we know it is oblique if true)
            print("Oblique Triangle")
        if angle_a_int < 90 and angle_b_int < 90 and angle_c_int < 90:
            print("Oblique Triangle") #tests for acute triangle (we know is oblique if true and not obtuse)
        print()
    cont = input("Do you wish to process another triangle (Y or N)? ").lower() #asks if user wants to input another triangle
    print()
print("Number of valid triangles: " + str(count)) #prints number of valid triangles