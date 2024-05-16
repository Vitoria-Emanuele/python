menu = 'Menu'
print(menu.center(50))
print("1. Soma\n2. Subtracao\n3. Multiplicacao\n4. Divisao")
opcao = int(input("Digite uma das opcoes: "))
num = int(input("Digite o numero para gerar a tabuada: "))

if opcao == 1:
    print("Tabuada da Soma do %d" %(num))
    for i in range(0, 11):
        print("%d + %d = %d"%(i, num, i+num))
elif opcao == 2:
    print("Tabuada da Subtracao do %d" %(num))
    for i in range(0, 11):
        print("%d - %d = %d"%(i, num, i-num))
elif opcao == 3:
    print("Tabuada da Multiplicacao do %d" %(num))
    for i in range(0, 11):
        print("%d * %d = %d"%(i, num, i*num))
elif opcao == 4:
    print("Tabuada da Divisão Inteira do %d" %(num))
    for i in range(0, 11):
        if i%num == 0:
            print("%d / %d = %d"%(i, num, i/num))