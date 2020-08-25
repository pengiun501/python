import random
ans=random.randint(1,20)
i=0
while i<5:
    num=int(input('please input a number from 1 to 20:'))
    i=i+1
    if ans>num:
        print('太小了')
    elif ans<num:
        print('太大了')
    else:
        print('答對了')
        print('玩了',i,'次')
        break
else:
    print('超過次數了')
    print('遊戲結束')