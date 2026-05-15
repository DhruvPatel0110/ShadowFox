# Simulating rolling a six-sided die 20 times
import random

rolls = []
count_6 = 0
count_1 = 0
two_6_in_row = 0

for i in range(20):
    roll = random.randint(1, 6)
    rolls.append(roll)

    if roll == 6:
        count_6 += 1

    if roll == 1:
        count_1 += 1

for i in range(len(rolls) - 1):
    if rolls[i] == 6 and rolls[i + 1] == 6:
        two_6_in_row += 1

print("Dice Rolls :", rolls)
print("Number of times 6 rolled :", count_6)
print("Number of times 1 rolled :", count_1)
print("Two 6s in a row :", two_6_in_row)

# Random Output Each round : 
# Dice Rolls : [5, 5, 4, 6, 2, 5, 2, 1, 5, 2, 1, 6, 5, 6, 2, 4, 2, 5, 3, 2]
# Number of times 6 rolled : 3
# Number of times 1 rolled : 2
# Two 6s in a row : 0


# Jumping Jacks Workout Program
total_jumping_jacks = 100
completed = 0
for i in range(10, total_jumping_jacks + 1, 10):
    completed += 10

    if completed == 100:
        print("Congratulations! You completed the workout.")
        break

    tired = input("Are you tired? ")

    if tired == "yes" or tired == "y":
        skip = input("Do you want to skip the remaining sets? ")

        if skip == "yes" or skip == "y":
            print(f"You completed a total of {completed} jumping jacks.")
            break

    remaining = total_jumping_jacks - completed
    print(f"{remaining} jumping jacks remaining.")

# Output : 
# Are you tired? n
# 90 jumping jacks remaining.
# Are you tired? n
# 80 jumping jacks remaining.
# Are you tired? n
# 70 jumping jacks remaining.
# Are you tired? y
# Do you want to skip the remaining sets? n
# 60 jumping jacks remaining.
# Are you tired? y
# Do you want to skip the remaining sets? y
# You completed a total of 50 jumping jacks.