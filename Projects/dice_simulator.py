import random

print("=== Dice Simulator ===")

num_dice = int(input("How many dice do you want to roll? "))

results = []
for i in range(num_dice):
    roll = random.randint(1, 6)
    results.append(roll)

print("You rolled:", results)
print("Total:", sum(results))
