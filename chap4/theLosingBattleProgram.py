import random as rm

# 어텍 데미지 벨류 -10 ~ 20 .
# 만약 데미지 벨류가 음수이면 어택 fail
# 마지막에 총 라운드와 우승자 출력

heroHP , monHP = rm.randrange(50, 100), rm.randrange(50, 100)
print(f"hero HP {heroHP}, monster HP: {monHP}")
cnt = 0
while True:
    heroAT , monAT = rm.randrange(-10,20), rm.randrange(-10,20)
    print("hero(HP:{0}, attack:{1}) {2} <-> monster(HP:{3}, attack:{4}) {5}"
          .format(heroHP, heroAT, "success" if heroAT > 0 else "fail", monHP, monAT, "success" if monAT > 0 else "fail"))
    cnt += 1
    if heroHP <= 0 or monHP <= 0:
        break
    if heroAT > 0:
        monHP = monHP - heroAT
    elif monAT > 0:
        heroHP = heroHP - monAT
print("---------------------------------------------------\n")
print(f"Total phase: {cnt},")
print("Hero Win!!!!" if heroHP > 0 and monHP <= 0 else "Monster win!!!!")