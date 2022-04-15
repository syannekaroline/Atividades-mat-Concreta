#Escreva um programa para receber uma sequência numérica de números inteiros e informar a soma do subconjunto dos números que são maiores que o seu predecessor.

#receber uma sequencia
sequencia=list(map(int,input("Insira uma sequencia: ").split( )))

#realizar a soma do subconjunto dos números que são maiores que seus antecessores
soma=0
#percorrer cada número da sequencia
print("Subconjunto dos números maiores que seus predecessores: ")
for i in range(1,len(sequencia)):

    if sequencia[i]>sequencia[i-1]:#verificar se o número é maior que o se predecessor
        soma=soma+sequencia[i]
        print(sequencia[i],",",end="")

print("\nSoma do subconjunto dos números que são maiores que seus predecessores: " ,soma)