Math=int(input('please input Math score:'))
Eng=int(input('please input English score:'))
if Eng>=90 and Math>=90:
    print('有獎品')
elif Eng<=60 and Math<=60:
    print('要處罰')
elif Eng<=60 or Math<=60:
    print('再加油')