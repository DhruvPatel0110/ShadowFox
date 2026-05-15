# Creating a list of friends and tuples with name lengths
friends = ["Aditya", "Rahul", "Santosh", "Praful", "Karan"]

friend_tuples = []

for name in friends:
    friend_tuples.append((name, len(name)))

print("Friend Tuples :", friend_tuples)
# Output
# Fiend Tuples : [('Aditya', 6), ('Rahul', 5), ('Santosh', 7), ('Praful', 6), ('Karan', 5)]


# Creating expense dictionaries for you and your partner
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

print("\nYour Expenses :", your_expenses)
print("Partner Expenses :", partner_expenses)

# Output
# Your Expenses : {'Hotel': 1200, 'Food': 800, 'Transportation': 500, 'Attractions': 300, 'Miscellaneous': 200}
# Partner Expenses : {'Hotel': 1000, 'Food': 900, 'Transportation': 600, 'Attractions': 400, 'Miscellaneous': 150}


# Calculating total expenses
your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print("\nYour Total Expenses :", your_total)
print("Partner Total Expenses :", partner_total)

# Output
# Your Total Expenses : 3000
# Partner Total Expenses : 3050


# Finding who spent more
if your_total > partner_total:
    print("\nYou spent more money overall")

elif partner_total > your_total:
    print("\nYour partner spent more money overall")

else:
    print("\nBoth spent the same amount")

# Output
# Your partner spent more money overall

# Finding category with maximum expense difference
max_difference = 0
max_category = ""

for category in your_expenses:
    difference = abs(your_expenses[category] - partner_expenses[category])

    if difference > max_difference:
        max_difference = difference
        max_category = category

print("\nCategory with Highest Difference :", max_category)
print("Difference Amount :", max_difference)

# Output
# Category with Highest Difference : Hotel
# Difference Amount : 200