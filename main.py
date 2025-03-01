import random

ability_scores = [random.randint(3, 18) for i in range(0, 6)]
abilities = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]

print(f"You rolled the following scores: {ability_scores}")

chosen_stat = input(
"""Choose from the following options (use the abbreviation):
Strength(STR)
Dexterity(DEX)
Constitution(CON)
Intelligence(INT)
Wisdom(WIS)
Charisma(CHA)
Choice: """).upper()

print(f"You chose {chosen_stat} as the ability to assign")

