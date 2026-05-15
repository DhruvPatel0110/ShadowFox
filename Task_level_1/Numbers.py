# Function using format() for string formatting
def formatted_string(num, char):
    return "Formatted Output : {} and {}".format(num, char)

result = formatted_string(145, 'o')
print(result)
# Output : Formatted Output : 145 and o
# Representation Used : format() string formatting


# Calculating area of circular pond and total water
radius = 84
pi = 3.14

pond_area = pi * radius * radius
print(f"Area of Pond : {pond_area}")

water_per_sq_meter = 1.4
total_water = pond_area * water_per_sq_meter

print(f"Total Water in Pond : {int(total_water)} liters")

# Output : Area of Pond : 22155.84
# Output : Total Water in Pond : 31018 liters

# Calculating speed in meters per second
distance = 490
time = 7 * 60
speed = distance / time
print(f"Speed : {int(speed)} m/s")

# Output : Speed : 1 m/s