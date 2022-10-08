'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
result=0
subs=0
menu=0
saque=0
saldo=0
import os  
import time 

#MENU



while(menu!=5):
    menu = int(input("############## Bem vindo ao pyBanking ############## \n \nDigite a opcao desejada \n \n1 - Deposito \n2 - Saque \n3 - Saldo\n \n"))
    os.system ("clear")
    print('Por favor digite um comando valido')
    time.sleep(3)
    os.system ("clear")
#MENU 1 = SALDO
    if (menu==1):
        os.system ("clear")
        saldo = float(input("Digite o valor que deseja depositar \n \n"))
        os.system ("clear")
        print('Seu saldo atual é de R$',saldo)
        time.sleep(10)
        os.system ("clear")
#MENU 2 = SAQUE
    elif (menu ==2):
        os.system ("clear")
        saque = float(input("Digite o valor que deseja realizar o saque \n \n"))
        result = saque - saldo
        if(saque > saldo): 
            os.system ("clear")
            print ('Este saque não pode ser realizado pois você é pobre')
            time.sleep(10)
            os.system ("clear")
        else:
            subs = saldo - saque
            print('Realizado saque de R${}\n \nSeu saldo atual é de R${}'.format(saque,subs))
            time.sleep(10)
            os.system ("clear")

