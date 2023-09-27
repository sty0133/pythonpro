import random as rm

print("         Welcome to 'Guess My Number'!\n\nY'm thinking of a number between 1 and 100.\nTry to guess it in as few attempts as possible.\n")
random_num = rm.randrange(1,100)
n = 0
cnt = 0

#print(random_num)
while n != random_num:
    n = int(input("Take a guess: "))
    cnt += 1
    
    if n > random_num:
        print("Lower...")
    elif n < random_num:
        print("Higher")

print("You guessed it! The number was " + str(random_num) +
      "\nAnd it only took you "+ str(cnt) +" tries!")

input("\n\nPress the enter key to quit")
