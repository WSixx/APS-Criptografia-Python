
'''
Descriptografa um texto criptografado
'''

def descrip():

    n = int(input("Digite a chave N:\n---> "))
    d = int(input("Digite a chave D:\n---> "))

    def mod(a,b): # mod function
        if(a<b):
            return a
        else:
            c=a%b
            return c

    def descifra(cifra,n,d):
        lista=[]
        msgToDesc = 0
        i=0
        tamanho=len(cifra)
        # texto=cifra ^ d mod n
        while i<tamanho:
            msgToDesc = cifra[i]
            msgToDesc = int(msgToDesc)
            frase=msgToDesc**d ##𝑀=𝐶**𝑑 mod(𝑛)
            texto=mod(frase,n)
            letra=chr(texto)
            lista.append(letra)
            i=i+1
        return lista
    end =False
    while(end!=True):
        escolha = input("Escolha 1 para Descriptografar direto e 2 para digitar a MSG:\n---> ")
        
        if escolha == '1':
            f = open("encrypt.txt","r")
            if f.mode == 'r':
                msg = f.readlines()
        
            list2 = [el.replace('\n', '') for el in msg]
            f.closed
            end = True
        elif escolha == '2':
            teste = False
            aba = 0
            list2 = []
            while teste != True:
                pas = input("deseja continuar? S or N: ")
                pas.upper
                if pas == "s":
                    mem = int(input("Digite primeiro: "))
                    list2.append(mem)
                    aba = aba + 1
                    teste = False
                elif pas =="n":
                    test = True
                    end = True
                    break
        else:
            print("\33[0;37;41mEsolha inválida\033[0;37;40m")
        
    OriginalText = descifra(list2,n,d)
    print("Mensagem descriptografada: \n")
    print(''.join(map(str, OriginalText)))
  


