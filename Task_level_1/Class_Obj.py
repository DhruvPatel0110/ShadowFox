# Creating Avenger class with properties and methods
class Avenger:

    def __init__(self, name, age, gender, super_power, weapon, leader=False):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon
        self.leader = leader

    def get_info(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Gender : {self.gender}")
        print(f"Super Power : {self.super_power}")
        print(f"Weapon : {self.weapon}")

    def is_leader(self):
        if self.leader:
            print(f"{self.name} is a Leader")
        else:
            print(f"{self.name} is not a Leader")



# Creating superhero objects
captain_america = Avenger("Captain America", 100, "Male", "Super Strength", "Shield", True)

iron_man = Avenger("Iron Man", 48, "Male", "Technology", "Armor")

black_widow = Avenger("Black Widow", 35, "Female", "Superhuman", "Batons")

hulk = Avenger("Hulk", 49, "Male", "Unlimited Strength", "No Weapon")

thor = Avenger("Thor", 1500, "Male", "Super Energy", "Mjolnir")

hawkeye = Avenger("Hawkeye", 41, "Male", "Fighting Skills", "Bow and Arrows")



# Displaying superhero information
captain_america.get_info()
captain_america.is_leader()
# Output :
# Name : Captain America
# Age : 100
# Gender : Male
# Super Power : Super Strength
# Weapon : Shield
# Captain America is a Leader
print()

iron_man.get_info()
iron_man.is_leader()
# Name : Iron Man
# Age : 48
# Gender : Male
# Super Power : Technology
# Weapon : Armor
# Iron Man is not a Leader
print()

black_widow.get_info()
black_widow.is_leader()
# Name : Black Widow
# Age : 35
# Gender : Female
# Super Power : Superhuman
# Weapon : Batons
# Black Widow is not a Leader
print()

hulk.get_info()
hulk.is_leader()
# Name : Hulk
# Age : 49
# Gender : Male
# Super Power : Unlimited Strength
# Weapon : No Weapon
# Hulk is not a Leader
print()

thor.get_info()
thor.is_leader()
# Name : Thor
# Age : 1500
# Gender : Male
# Super Power : Super Energy
# Weapon : Mjolnir
# Thor is not a Leader
print()

hawkeye.get_info()
hawkeye.is_leader()
# Name : Hawkeye
# Age : 41
# Gender : Male
# Super Power : Fighting Skills
# Weapon : Bow and Arrows
# Hawkeye is not a Leader