print("\n                        Trust Fund Buddy\nTotals your monthly spending so that your trust fund doesn't run out\n<and you're forced to get a real job>.\n\nPlease enter the requested, monthly costs. Since you're rich, ignore pennies\nand use only dollar amounts.\n")
ltu = int(input("Lamborghini Tune-Ups: "))
ma = int(input("Manhattan Apartment: "))
pjr = int(input("Private Jet Rental: "))
g = int(input("Gifts: "))
d = int(input("Dinning Out: "))
s = int(input("Staff <butlers, chef, driver, assistant>: "))
pgc = int(input("Personal Guru and Coach: "))
cg = int(input("Computer Games: "))

print("Grand Total:  ",ltu+pjr+g+d+s+pgc+cg)
