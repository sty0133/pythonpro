ls = [["Larry" , 1500] , ["Moe" , 1000]]
while True:
    print("\tHige Scores Keeper\n\n\t0 - Quit\n\t1 - List Scores\n\t2 - Add a Score\n")
    ch = int(input("Choice: "))
    print()
    if ch == 1:
        ls.sort(key=lambda x : -x[1])
        print("High Scores\n\nName\tSCORE")
        for i in range(len(ls)):
            for j in ls[i]:
                print(j , end="\t")
            print()
        print()
    elif ch == 2:
        nm = input("What is the player's name?: ")
        sc = int(input("What score did the player get?: "))
        ls_new = [nm , sc]
        ls.append(ls_new)
    elif ch == 0:
        exit()
    else:
        continue