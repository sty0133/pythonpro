import random as rm

words = ('difficult', 'banana', 'apple', 'python', 'daegu', 'catholic', 'university')
word = words[rm.randrange(0,6)]
sh_word = list(word)
rm.shuffle(sh_word)
# print(sh_word)

print("Welcome to Word Jumble!\nUnscramble the letters to make a word.\njumble word: {0}".format(''.join(sh_word)))
if input("Your gueuss: ") == word:
    print("Good, that's correct!")
else:
    print("Sorry, that's not correct. The word was: {0}".format(word))

