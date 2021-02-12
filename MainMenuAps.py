import secrets
import pyfiglet
import os
from EncryptDecryptTeste import cryptDecrypt
from GerarPrimes import Gerar
from Decrypt import descrip
from Encrypt import Criptografar


'''
Criado Por: Lucas

'''

os.system('cls')
result = pyfiglet.figlet_format("\nCriptografia Python", font = "slant" )
print(result)
print("")

def main():
    end = False
    escolha = 0
    while(end!=True):
        print('\n######################################')
        print('#    1.) TESTE||Encrypt||Decrypt     #')
        print('#    2.) Gerar números Primos        #')
        print('#    3.) Criptografar                #')
        print('#    4.) descriptografar             #')
        print('#    5.) \33[0;37;41mSair\033[0;37;40m                       #')
        print('######################################')
        try:
            escolha = int(input('---> '))
        except:
            print('\33[0;37;41mDigite uma opção válida\033[0;37;40m')
        if(escolha == 1):
            cryptDecrypt()
        elif(escolha == 2):
            numpri = int(input("Digite a quantidade(Range) de primos para gerar: "))
            Gerar(numpri)
        elif(escolha == 3):
            Criptografar()
        elif(escolha == 4):
            descrip()
        elif(escolha == 5):
            end = True

if __name__ == '__main__':
    main()