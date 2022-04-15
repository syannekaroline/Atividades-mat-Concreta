#Escreva um programa para receber uma sequência numérica de números naturais e informar a soma do subconjunto dos números primos.
#receber uma sequencia
sequencia=list(map(int,input("Insira um quência de números inteiros: ").split( )))

#percorrer a sequencia
#realizar a soma se o número for primo
soma=0
for i in range(len(sequencia)):

    #verificar se o número é primo( se é divisível apenas por ele msm e por 1, ou seja, tem apenas 2 divisores)
    #contar quantos divisores o número tem
    ndiv=0
    for c in range(1,sequencia[i]+1):#soma no fim do range pois o último número precisa ser dividido por ele mesmo
        if sequencia[i]%c==0:#se o resto da divisão do número for igual a 0 
            ndiv+=1
    if ndiv==2:#se o número tiver só 2 divisores é pq é primo
        soma=soma+sequencia[i]
        print(sequencia[i],",",end="")
    
print("\nSoma do subconjunto dos números primos: ",soma)