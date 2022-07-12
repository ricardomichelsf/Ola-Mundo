num1= int(input())
while num1 <1 or num1 > 9:
    print('Insira um número inicial entre 1 e 9')
    num1= int(input())

num2= int(input())
while num2 <1 or num2 > 9:
    print('Insira um número final entre 1 e 9')
    num2= int(input())

if num1 > num2:
    print('Nenhuma tabuada nesse intervalo')
else:
    while num1 <= num2:
        cont=1
        while cont <= 9:
            print('{} x {} = {}'.format(num1, cont, num1*cont))
            cont +=1
        print('')
        num1 +=1