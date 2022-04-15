#Escreva um programa para receber uma sequência numérica de números inteiros e informar a soma do subconjunto dos números pares.

#receber uma sequencia
sequencia=list(map(int,input("Insira um seuquência de números inteiros: ").split( )))

#informar o subconjunto dos nuúmeros pares
print("Subconjunto dos números pares: ")

#percorrer a sequência
for i in range(len(sequencia)):
    if sequencia[i]%2==0:#verifica se o resto da divisão por 2 é zero, ou seja, se o número é par
        print(sequencia[i],",",end=(""))#imprime os números pares da sequência
    