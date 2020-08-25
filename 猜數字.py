import random
ans=random.randint(1,10)
num=int(input('please input a number from 1 to 10:'))
if ans==num:
    print('你猜對了!')
    print('恭喜!!')
else:
    print('你猜錯了...')
    print('正確答案是:',ans)