import secrets
import sys
import time

def Criptografar():

        p = 0
        q = 0

        def primo(num):
            divisores = 0
            i = 1
            while i <= num:
                if num % i == 0 :
                    divisores = divisores + 1
                i = i + 1

            if divisores == 2:
                return True
            else:
                return False

        def mod(a,b): # mod function
            if(a<b):
                return a
            else:
                c=a%b
                return c

        '''
        Cifra um texto
        '''
        '''
        E= Maior que 1 e menor que (p-1)
            não ter dfator comum de (p-1) e (q-1) exceto 1
            basta  escolhermos  um  número  que  satisfaça 1>𝑒>𝜑(𝑛)e 𝑑(𝑒)𝑑(𝜑𝑛)ou  seja,  que  esteja  entre  1
            e  o  valor  que encontramos anteriormenteenão possuadivisores comuns (além do 1, claro) com ele
        '''
        def gerarE(num): # recives totient of N as a parameter
            def mdc(n1,n2): # compute the mdc of the totient of N and E
                resto=1
                while(n2!=0):
                    resto=n1%n2
                    n1=n2
                    n2=resto

                return n1

            while True:
                cryptogen = secrets.SystemRandom()
                e=cryptogen.randrange(2,num) # define the range of the E
                if(mdc(num,e)==1):
                    return e

        def cript(frase,e,n): #
            tam=len(frase)
            i=0
            lista=[]
            while(i<tam):
                letter=frase[i]
                k=ord(letter) # passei para asc
                k=k**e  #𝐶=𝑀**𝑒 mod(𝑛)
                d=mod(k,n)
                lista.append(d)
                i=i+1
            return lista

        '''
        Calcula a chave privada
        '''
        '''
        Private Key d is calculated from the numbers p, q and e.
        ed = 1 mod (p-1) (q-1)
        The above formula is the basic formula for Extended Euclidean Algorithm,
        which takes p and q as the input parameters.
        '''
        def private_key(toti,e):
            d=0
            while(mod(d*e,toti)!=1):   #ed = 1 mod (p-1) (q-1)  -- é o E e o Toti -
                d += 1 #The multiplicative inverse of a modulo m exists if and only if a and m are coprime (i.e., if gcd(a, m) = 1)
            return d


        f= open("encrypt.txt","w+")
        textoFile = input("Digite o texto para salvar no arquivo e ser criptografado: \n---> ")
        f.write(textoFile)
        f.close()

        f = open("encrypt.txt","r")
        if f.mode == 'r':
            msg =f.read()

        print("\n")
        prime = False
        while prime != True:
            p = int(input("Digite o primeiro numero primo:\n---> "))
            q = int(input("Digite o segundo número primo:\n---> "))
            #Aqui fazer validação se o numero é primo
            if primo(q) and primo(p) and q != p:
                prime = True
            else:
                print("Apenas Primos não iguais por favor - Digite novamente")
                prime = False

        print("\n")
        start_time = time.time()
        n = p*q # calculo N
        totienteN = (p-1) * (q-1)
        e = gerarE(totienteN) #  E
        public_key = (n, e)

        print("=========================================================================================================")
        print('Chave pública:', public_key, "\n")
        textCipher = cript(msg,e,n)
        print("=========================================================================================================")
        print('Mensagem criptografada:', textCipher, "\n")
        d = private_key(totienteN,e)

        with open('encrypt.txt', 'w') as f:
            for item in textCipher:
                f.write("%s" % item + "\n")

        print("=========================================================================================================")
        print("p:", p, "q:", q)
        print("n:", n)
        print("d:", d)
        print("=========================================================================================================")
        f.closed
        print("\nTempo: " + "---\33[0;37;41m %s \033[0mseconds --- \n" % (time.time() - start_time))
        print("=========================================================================================================")
        ##Melhorar o desempenho dos metodos
