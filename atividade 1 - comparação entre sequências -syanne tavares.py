#algoritmo que recebe duas sequências e faz a comparação entre elas informando ao usuácio se as sequências são iguais ou diferentes e imprimir o número de instruções usadas.
print(f'{"comparação entre sequências":=^60}')

num_instrucoes=0#declara a variável que vai contar o número de instruções usadas

#receber a primeira sequência
sequencia1=input("Insira a primeira sequência : ").split( )#split adiciona elementos ao final de uma lista
num_instrucoes+=1
#receber a segunda sequência.
sequencia2=(input("Insira segunda sequência : ").split())
num_instrucoes+=1

# função que fará a comparação entre as sequências
def compara_sequencias(sequencia1,sequencia2,nun_intrucoes):
  # compara o tamanho das sequências

  if len(sequencia1) != len(sequencia2):#se tiverem tamanhos diferentes
    #retorna ao usuário a mensagem a baixo
    print("As sequências são diferentes, não possuem o mesmo tamanho.")
    nun_intrucoes+=1
    print("Numero de Instruções usadas:",(nun_intrucoes+1))  

  else:#se tiverem o mesmo tamanho
    num_instrucoes=+1  
    #um laço é criado pra percorrer as duas sequências e comparar elemento por elemento

    for i in range(len(sequencia1)):
      num_instrucoes=+1

      #verifica se os elementos são diferentes
      if sequencia1[i]!=sequencia2[i]:
        num_instrucoes+=1

        #mostra a mensagem indicando que são diferentes
        print("As sequências são diferentes pois tem elementos diferentes na posição %d" %(i))
        num_instrucoes+=1

        #mostra o número de instruções usadas
        print("Numero de Instruções usadas:",(num_instrucoes))
        break

      elif i == (len(sequencia1)-1):#se as sequências forem iguais e a comparação estiver no último elemento da sequência
        num_instrucoes+=1

        #mostra que são iguais e o número de instruções usadas

        print("As sequencias são iguais !!")
        num_instrucoes+=1
        print("Numero de Instruções usadas:",(num_instrucoes+1))

print(compara_sequencias(sequencia1,sequencia2,num_instrucoes))#chama a função de comparação de sequências com os 3 parâmetros que serão usados e imprime o resultado da comparação