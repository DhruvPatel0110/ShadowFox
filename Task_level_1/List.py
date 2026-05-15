# Creating the Justice League list
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

print("Initial List :", justice_league)

# Calculating number of members
print("\nNumber of Members :", len(justice_league))
#output: Number of Members : 6

# Adding Batgirl and Nightwing
justice_league.append("Batgirl")
justice_league.append("Nightwing")

print("\nAfter Adding Members :", justice_league)

# Moving Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")

print("\nAfter Making Wonder Woman Leader :", justice_league)

# Separating Aquaman and Flash using Green Lantern
justice_league.remove("Green Lantern")
flash_index = justice_league.index("Flash")
justice_league.insert(flash_index, "Green Lantern")

print("\nAfter Separating Aquaman and Flash :", justice_league)

# Replacing the old team with new members
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("\nNew Justice League Team :", justice_league)

# Sorting the list alphabetically
justice_league.sort()

print("\nSorted Justice League :", justice_league)

# Finding the new leader
print("\nNew Leader :", justice_league[0])
# Output : Cyborg