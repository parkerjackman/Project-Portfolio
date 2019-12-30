# Parker Jackman
#Assn 4
# Cuboid Calculator

print("Welcome to the Cuboid Calculator!")
print("Please enter values in feet.")
print("")

length = eval(input("Enter the length: "))
width = eval(input("Enter the width: "))
height = eval(input("Enter the height: "))

volume = length * width * height
surface_area = 2 * length * width + 2 * length * height + 2 * width * height

print("")

print("Your", length, "X", width, "X", height, "cuboid has a volume of", volume,
      "cubic feet and a surface area of", surface_area, "square feet.")