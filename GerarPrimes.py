import secrets
def Gerar(n):
        print("Gerar numeros primos até: ", n, ":\n")
        """ Returns  a list of primes < n """
        sieve = [True] * n
        for i in range(3,int(n**0.5)+1,2):
            if sieve[i]:
                sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
        print( [2] + [i for i in range(3,n,2) if sieve[i]])
        textoFile2 = [2] + [i for i in range(3,n,2) if sieve[i]]
        print("\033[1;34;40mRandom Choice 1:",secrets.choice(textoFile2),"Random Choice 2:", secrets.choice(textoFile2), "\033[0;37;40m")
        f= open("primos.txt","w")
        for item in textoFile2:
            f.write("%s" %item + "\n")
        f.close()
