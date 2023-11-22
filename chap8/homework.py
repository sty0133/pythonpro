text_file = open("./homework.txt", "r")
text = text_file.readlines()
print("\t\tWlcome to Trivia Challenge!\n\n")

def prob():
    print(f"\t\t{text[0]}\n\n{text[1]}\n{text[2]}\n\t1 - {text[3]}\n\t2 - {text[4]}\n\t3 - {text[5]}\n\t4 - {text[6]}\n")

def answer():
    num = input("What's your answer?: ")
    print()
    return right(num)

def right(num):
    if num == text[7]:
        print("You are Genious!")
    else:
        print("Try again...!")
        answer()

prob()
answer()