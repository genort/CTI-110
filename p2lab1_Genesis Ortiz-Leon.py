#Genesis Ortiz-Leon
#9/14/26
#P2LAB1
#Calculating a circle's radius, diameter,circumference and area.

import math

#Get radius
radius = float(input("Enter the radius of the circle:"))

#Calculate the data type of a variable
print(type(radius))

#Calculate diameter
diameter = radius * 2
print(f"The diameter of the circle is: {diameter:.1f} ")

#Calculate the circumference
circ = 2 * math.pi * radius
print(f"The circumference of the circle is: {circ:.2f} ")

#Calculate the area
area = math.pi *radius ** 2
print(f"The area of the circle is: {area:.3f}")
