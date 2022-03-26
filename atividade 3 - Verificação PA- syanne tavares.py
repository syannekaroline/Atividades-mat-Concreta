# algoritmo que verifica se uma sequência é uma progressão aritmética e a classifica.

#título pro usuário saber do que se trata o programa
print('{:=^60}'.format(" Verificação de PA e classificação "))
#declaração das variáveis que serão utilizadas
sequencia=[]#lista que guardará a sequência recebida
pa="PA"#string que verificará se a sequência é uma PA

#recebe a sequência

#A sequência vai receber uma lista, a função map vai aplicar a função inteiro pra todos os elementos inseridos no input, os elementos no input serão divididos por um espaço devido a função split.

sequencia=list(map(int,input("Insira a sequência  : ").split( )))

print(sequencia)
                    
#verificar se é PA
    #comparar se cada elemento tem mesma razão
    #achar a suposta razão

r = (sequencia[1]-sequencia[0])
       #subtrair o elemento 1 do elemento 0 e apartir disso:
 
for i in range(len(sequencia)):
  #subtrair um elemento do seu antecessor para todos os elementos apartir do primeiro e comparar o resultado coa razão.
  if sequencia[i]-sequencia[i-1] != r :
    #se uma sub for diferente da razão entao nao é pq caso contrário é
    pa="A sequência não é uma PA."
  else:
    pa="A sequencia é uma PA."
    
 #classificar o tipo de Pa
if pa=="A sequencia é uma PA.":
  
  #PA crescente => r>0
  if(r>0):
    print("A sequência é uma PA crescente.")
  #PA descrescente => r<0
  if(r<0):
    print("A sequência é uma PA decrescente.")
  
  #PA constante r=0
  if(r==0):
    print("A sequência é uma PA constante.")
else:
  print("A sequencia não é uma PA")