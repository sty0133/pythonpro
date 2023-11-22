import random as rm
#Homework 1
class Critter:
    def Name():
        global name
        name = input("What do you wnat to name your critter?: ")
        print()
    def setMood(level):
        global Mood_level
        Mood_level = level
    def Talk():
        global name
        global Mood_level
        Mood_level -= rm.randrange(1,4)
        if Mood_level <= 5:
            print(f"\nI'm {name} and I feel mad now.\n")
        elif Mood_level <= 10 and Mood_level > 5:
            print(f"\nI'm {name} and I feel frustrated now.\n")
        elif Mood_level > 10 and Mood_level < 40:
            print(f"\nI'm {name} and I feel happy now.\n")
        elif Mood_level >= 40:
            print("BOOOOOOOOOOOM! I'm so HIGH!!!")
    def Feed():
        global Mood_level
        print("\nYummy~")
        Mood_level += 2
        rm.randrange(1,3)
    def Play():
        global Mood_level
        print("\nWheee!")
        Mood_level += rm.randrange(1,3)
    def getMood():
        while True:
            print("\tCritter Caretaker\n\n\t0 - Quit\n\t1 - Listen to your critter\n\t2 - Feed your critter\n\t3 - Play with your critter\n")
            choice = int(input("Choice: "))
            if choice == 0:
                break
            elif choice == 1:
                Critter.Talk()
            elif choice == 2:
                Food.Name()
            elif choice == 3:
                Critter.Play()

#Homework 2
class Food:
    def Name():
        global food
        print("\t\t1 . BANANA\n")
        print("\t\t2 . APPLE\n")
        print("\t\t3 . BEEF\n")
        food = int(input("\nWhat food do you want to give?: "))
        Food.setCritterLevel(food)

    def setCritterLevel(food):
        global Mood_level
        if food == 1:
            print("Weee!!! I love banana!\n")
            Mood_level += rm.randrange(1,3)
        elif food == 2:
            print("Weee!!! I love apple!\n")
            Mood_level += rm.randrange(2,4)
        elif food == 3:
            print("Weee!!! I love beef!\n")
            Mood_level += rm.randrange(3,6)
        else:
            print(f"There is no number {food}. Please try again.\n")
            return Food.Name()

        



Critter.Name()
Critter.setMood(rm.randrange(1,10))
Critter.getMood()
    
