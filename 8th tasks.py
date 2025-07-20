class Avenger:
    def __init__(self, name, age, gender, super_power, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon

    def get_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Super Power: {self.super_power}")
        print(f"Weapon: {self.weapon}")
        print("-" * 30)

    def is_leader(self):
        return self.name == "Captain America"


super_heroes = [
    Avenger("Captain America", 100, "Male", "Super strength", "Shield"),
    Avenger("Iron Man", 48, "Male", "Technology", "Armor"),
    Avenger("Black Widow", 35, "Female", "Superhuman", "Batons"),
    Avenger("Hulk", 40, "Male", "Unlimited Strength", "No Weapon"),
    Avenger("Thor", 1500, "Male", "Super Energy", "Mjölnir"),
    Avenger("Hawkeye", 38, "Male", "Fighting Skills", "Bow and Arrows")
]

for hero in super_heroes:
    hero.get_info()
    if hero.is_leader():
        print(f"{hero.name} is the leader of the Avengers.")
    else:
        print(f"{hero.name} is not the leader.")
    print()
