from random import *
apply = range(1,21)
apply = list(apply)
shuffle(apply)


apply1=sample(apply,1)
print("치킨 담청자는 "+str(apply1) + "지원자입니다.")
apply2=sample(apply,3)
print("zjvl 담청자는 "+str(apply2) + "지원자입니다.")
print("-------------------")

winners = sample(apply,4)
print("---당첨자발표---")
print("치킨 당첨자: {0}".format(winners[0]))
print("커피 당첨자: {0},{1},{2}".format(winners[1],winners[2],winners[3]))



