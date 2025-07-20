Count Justice League Members
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print(" Original members:", justice_league)
print("Number of members:", len(justice_league))

Add Batgirl and Nightwing
justice_league.extend(["Batgirl", "Nightwing"])
print("After adding Batgirl and Nightwing:", justice_league)
 

Move Wonder Woman to the Beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print(" Wonder Woman as leader:", justice_league)

Move Green Lantern between Aquaman and Flash

justice_league.remove("Green Lantern")
flash_index = justice_league.index("Flash")
justice_league.insert(flash_index, "Green Lantern")
print("After separating Aquaman and Flash:", justice_league)



Replace with New Justice League Members
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("New team:", justice_league)

Justice League Sorting
justice_league = ["Batman", "Superman", "Wonder Woman", "Flash", "Aquaman", "Cyborg"]
print("Original list:", justice_league)
justice_league.sort()
print("Sorted list:", justice_league)
print("New leader is:", justice_league[0])