'''
Escreva um programa para receber uma sequência numérica de números
inteiros e dois valores x e y, tal que: x ≠ y e 2 ≤ x, y < n, onde n> 10 é o tamanho da
sequência. Considerando os valores de entrada, aplique a decomposição da lista e exiba
os três subconjuntos gerados ordenados em ordem crescente, de acordo com o valor da
soma de cada subconjunto.
'''
#receber sequencia
sequencia=list(map(int,input("Insira uma sequência com mais de 10 elementos: ").split( )))

#receber um valor x
x=int(input("Insira um valor x maior ou igual a 2: "))

#receber um valor y
y=int(input("Insira um valor y diferente de x e maior que o tamanho da sua sequência: "))

#aplicar a decomposição da lista em subsequências
subseq1=sequencia[:x]
subseq2=sequencia[y:]
subseq3=sequencia[x:y]


#exibir os 3 subconjuntos gerados em ordem crescente de acordo com o valor da soma de cada subconjunto
def soma(subseq):#função que realiza a soma de sequências
    soma=0
    for x in subseq:
        soma=soma+x
    return soma

#comparação do tamanho de cada seuquência e organização por ordem crescente
if soma(subseq1)>soma(subseq2):
    aux=list(subseq1)
    subseq1=list(subseq2)
    subseq2=list(aux)
if soma(subseq1)>soma(subseq3):
    aux=list(subseq1)
    subseq1=list(subseq3)
    subseq3=list(aux)
if soma(subseq2)>soma(subseq3):
    aux=list(subseq2)
    subseq2=list(subseq3)
    subseq3=list(aux)

#exiba os três subconjuntos gerados ordenados em ordem crescente, de acordo com o valor da soma de cada subconjunto.
print(f"Subsequência  1: {subseq1} | soma: {soma(subseq1)}\nSubsequência  2: {subseq2} | soma: {soma(subseq2)}\nSubsequência  3: {subseq3} | soma : {soma(subseq3)}")