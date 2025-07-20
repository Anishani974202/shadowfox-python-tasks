Simulate Rolling a Six-Sided Die
import random
rolls = [random.randint(1, 6) for _ in range(20)]
print("Dice rolls:", rolls)
count_6 = rolls.count(6)
count_1 = rolls.count(1)
consecutive_6s = 0
for i in range(len(rolls) - 1):
    if rolls[i] == 6 and rolls[i + 1] == 6:
        consecutive_6s += 1
print("Times rolled 6:", count_6)
print("Times rolled 1:", count_1)
print("Consecutive 6s:", consecutive_6s)


5.1 Jumping Jacks Simulation
total_jacks = 0

while total_jacks < 100:
    total_jacks += 10
    print(f"You did {total_jacks} jumping jacks.")

    if total_jacks == 100:
        print("Congratulations! You completed the workout.")
        break
   tired = input("Are you tired? (yes/y or no/n): ").lower()
    if tired in ["yes", "y"]:
        skip = input("Do you want to skip the remaining sets? (yes/y): ").lower()
        if skip in ["yes", "y"]:
            print(f"You completed a total of {total_jacks} jumping jacks.")
            break