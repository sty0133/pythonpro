def frequency_analytic(word):
    sep_words = list(word)
    sep_words_lower = []
    sep_words_upper = []

    sep_words.sort(reverse=False)
    
    for word in sep_words:
        if word.islower() == True:
            sep_words_lower.append(word)
        else:
            sep_words_upper.append(word)
    sep_words_lower.sort(reverse=False)
    sep_words_upper.sort(reverse=False)
    # print(sep_words_lower)
    # print(sep_words_upper)

    sep_words = sep_words_lower + sep_words_upper
    dic = {}
    for a in sep_words:
        if a in dic:
            pass
        else:
            dic[a] = sep_words.count(a)

    # print(dic)
    for word, val in dic.items():
      print(word,val,end="\n")


if __name__ == "__main__":
    msg = input('input your message: ')
    frequency_analytic(msg)