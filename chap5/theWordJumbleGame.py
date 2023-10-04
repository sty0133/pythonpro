import random as rm
print("\n\t  Welcome to Word Jumble!\n\n  Unscramble the letters to make a word.\n<Press the enter key at the prompt to quit.>\n")
word = "difficult"
word_ls = list(word)
# print(word_ls)
rm.shuffle(word_ls)
# print(word_ls)
print("The jumble is: " + ''.join(word_ls))
word_input = input("\nYour guess: ")
# print(list(word_input))
# print(word)
if word == word_input:
    print(True)
else:
    print(False)
