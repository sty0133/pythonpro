# 1
inven = ["sword", "armor", "shield", "healing potion"]
print("Your items:")
for itmes in inven:
    print(itmes)

# 2    
input("\nPress the enter key to continue.")
print("You have {0} items in your possession.".format(len(inven)))

# 3
input("\nPress the enter key to continue.")
if "healing potion" in inven:
    print("You will live to fight another day.\n")

# 4
i = input("Enter the index number for an item in inventory: ")
print("At index {0} is {1}\n".format(i, inven[int(i)]))

# 5
fst = input("Enter the index number to begin a slice: ")
end = input("Enter the index number to end tje slice: ")
 
# for i in inven[int(fst):int(end)]:
#     print("'{}'".format(i))
print("inventory[ {0} : {1} ]                   [".format(fst , end),end="")
cnt = 0
ls_ind = inven[int(fst):int(end)]
# print(len(ls_ind))
for i in ls_ind:
    print("'{0}'".format(i),end="")
    cnt += 1
    if cnt < len(ls_ind):
        print(",",end=" ")
print("]")
# 6
input("\nPress the enter key to continue.")
chest = ["gold" , "gems"]
# 7
print("You find a chest. It contains:\n[",end="")
cnt_0 = 0
for h in chest:
    print("'{}'".format(h),end="")
    cnt_0 += 1
    if cnt_0 < len(chest):
        print(",",end="") 

print("]\nYou add the contents of the chest to your inventory.\nYour inventory is now:\n[",end="")
cnt_1 = 0
inven.extend(chest)
for j in inven:
    print("'{}'".format(j),end="")
    cnt_1 += 1
    if cnt_1 < len(inven):
        print(",",end="")
print("]")

input("\nPress the enter key to continue.")
print("You trade your sword for a crossbow./your inventory is now:\n[",end="")
inven[0] = "crossbow"
cnt_2 = 0
for j in inven:
    print("'{}'".format(j),end="")
    cnt_2 += 1
    if cnt_2 < len(inven):
        print(",",end="")
print("]")

input("\nPress the enter key to continue.")
print("You use your gold and gems to buy an orb of future telling.\nYour inventory is now:\n[",end="")
inven.remove("gold")
inven.remove("gems")
inven.append("orb of future telling")
cnt_3 = 0
for j in inven:
    print("'{}'".format(j),end="")
    cnt_3 += 1
    if cnt_3 < len(inven):
        print(",",end="")
print("]")
input("\nPress the enter key to continue.")
print("In a great battle, your shield is destroyed.\nYour inventory is now:\n[",end="")
inven.remove("shield")
cnt_4 = 0
for j in inven:
    print("'{}'".format(j),end="")
    cnt_4 += 1
    if cnt_4 < len(inven):
        print(",",end="")
print("]")

input("\nPress the enter key to continue.")
print("Your crossbow and armor are stolen by thieves.\nYour inventory is now:\n[",end="")
inven.remove("crossbow")
inven.remove("armor")
cnt_5 = 0
for j in inven:
    print("'{}'".format(j),end="")
    cnt_5 += 1
    if cnt_5 < len(inven):
        print(",",end="")
print("]")

input("\n\nPress the enter key to exit.")