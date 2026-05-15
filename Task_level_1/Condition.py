# BMI Category Calculator
height = float(input("Enter height in meters : "))
weight = float(input("Enter weight in kilograms : "))

bmi = weight / (height ** 2)

if bmi >= 30:
    print("Obesity")

elif bmi >= 25 and bmi <= 29:
    print("Overweight")

elif bmi >= 18.5 and bmi < 25:
    print("Normal")

else:
    print("Underweight")
# output: 
# Enter height in meters : 1.75
# Enter weight in kilograms : 80
# Overweight

# Finding country based on city name
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city = input("Enter a city name : ")

if city in Australia:
    print(f"{city} is in Australia")

elif city in UAE:
    print(f"{city} is in UAE")

elif city in India:
    print(f"{city} is in India")

else:
    print("City not found")

# Output
# Enter a city name : mumbai
# City not found --> Case Sensitive


# Checking whether two cities belong to the same country
city1 = input("Enter the first city : ")
city2 = input("Enter the second city : ")

if city1 in Australia and city2 in Australia:
    print("Both cities are in Australia")

elif city1 in UAE and city2 in UAE:
    print("Both cities are in UAE")

elif city1 in India and city2 in India:
    print("Both cities are in India")

else:
    print("They don't belong to the same country")

# Output
# Enter the first city : Mumbai
# Enter the second city : Delhi
# Both cities are in India