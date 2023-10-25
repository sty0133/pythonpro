word = ["Uninstalled"]
mean = ["Uninstalled means being fired. Especially popular during the dot-bomb era."]

while True:
    print("\tGeek Translator\n\n\t0 - Quit\n\t1 - Look Up a Geek Term\n\t2 - Add a Geek Term\n\t3 - Redefine a Geek Term\n\t4 - Delete a Geek Term")
    ch = int(input("\nChoice: "))
    print()
    if ch == 1:
        for i in range(len(word)):
            print(f"{i + 1}. {word[i]}\n{mean[i]}")
            print()
        print()
    elif ch == 2:
        nw = str(input("What is the Word: "))
        mn = str(input("What doed it mean: "))
        print()
        word.append(nw)
        mean.append(mn)
    elif ch == 3:
        fw = input("What is the Word: ")
        if fw in word:
            mean[word.index(fw)] = input("Redefine the mean: ")
            print()
        else:
            # print(fw)
            # print(ls.index(fw))
            print(f"There is no word {fw} in Geek Translator. Please add the word\n")
    elif ch == 4:
        dw = input("What word do you want to delete: ")
        # del ls[dw]
        if dw in word:
            # print(word.index(dw))
            mean.remove(mean[word.index(dw)])
            word.remove(dw)
            print(f"The word {dw} has been deleted.\n")
        else:
            print(f"There is no word {fw} in Geek Translator. Please add the word\n")
        
    elif ch == 0:
        exit()
    else:
        continue