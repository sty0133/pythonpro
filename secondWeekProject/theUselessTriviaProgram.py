name = input("Hi, What's your name? ")
age = int(input("And how old are you? "))
weigh = int(input("Okay, last question. How many killograms do you weigh? "))
print("\nDid you know that you're just "+str(round(age/7,1))+" in dog years?\n")
print("But  you're also over "+str(round(age*365*24*60*60,1))+" seconds old.\n")
print("If a small child were trying to get you attention, your name would become:\n"+name+name+name+name+"\n")
print("Did you know that on the moon you would weigh only "+str(round(weigh/6,1))+" killograms?\nBut on the sun, you'd weigh "+str(weigh*28)+" <but, ah... not for long>.\n\n")
input("Press the enter key to exit.")

