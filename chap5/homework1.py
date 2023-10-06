import random as rm

words = ('difficult', 'banana', 'apple', 'python', 'daegu', 'catholic', 'university')
word = list(rm.choice(words))
# print(word)
guess = ['_'] * len(word)
cnt = len(word)

# def wordindex(x):
#     return int(word.index(x))

# intro
print("Guess the Word!!!\nIn this game,the program selects a word at random, and player's objective is to guess the chosen word.\n\nLength of the selected word: {}".format(len(word)))

while cnt > 0:
    if guess == word:
        print("Congratulation! You guessed the word:","".join(word))
        exit()
    else: 
        print("Remaining attempts:",cnt)
        print("Current guessed word:"," ".join(guess))
    guesses = input("Guess a letter: ")
    if guesses in word:
        # print(word.index(guesses))
        nls = list(filter(lambda x: word[x] == guesses, range(len(word))))
        # print(nls)
        for x in nls:
            guess[x] = guesses

    cnt -= 1
    if cnt == 0 and word != guess:
        print("Incorrect guess.\nYou've used all your attempts. The correct word was {}.".format("".join(word)))
    
