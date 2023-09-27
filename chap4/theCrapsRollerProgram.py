import random as rm

dice1 = rm.randrange(1,6)
dice2 = rm.randrange(1,6)
sum = dice1 + dice2

print(f"You rolled a {dice1} and a {dice2} for a total of {sum}")
input("\n\nPress the enter key to quit.")