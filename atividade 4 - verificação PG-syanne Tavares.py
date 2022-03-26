#algoritmo que recebe uma sequencia verificando se é uma PG e classificando-a

print('{:=^60}'.format(" Verificação de PG "))
#declara as variáveis que serão usadas
sequencia=[]#lista que guardará a sequência inserida
pg="PG"#string que guardará a informação se a sequẽncia se trata de uma PG

#recebe a sequência
sequencia=list(map(int,input("Insira a sequência: ").split( )))
                   
#verificar se é PG
    #comparar se cada elemento tem mesma razão

    #achar a suposta razão
q = (sequencia[1]/sequencia[0])

#verificando se é PG estacionária
estacionário=False
for i in range (1,len(sequencia)):
  while sequencia[i] == 0:
    estacionário = True
    if sequencia[i] != 0:
      estacionário = False
    break
    
#se for uma sequência estácionária, informar ao usuário:
if estacionário==True:
  print("A sequência é uma PG estácionária de razão 0.")

#se não for estácionária
else:
  for i in range(2,len(sequencia)):#laço pra percorrer a sequẽncia
  #subtrair um elemento do seu antecessor para todos os elementos apartir do primeiro e comparar o resultado com suposta razão.
    if (sequencia[i]/sequencia[i-1]) != q :
      #se uma subtração for diferente da razão então nao é pg, caso contrário é PG
      pg="A sequência não é uma PG."
    else:
      pg="A sequência é uma PG."

   #classificar o tipo de PG de acordo com a razão encontrada se a sequencia for uma PG
  if pg=="A sequência é uma PG.":
    
    if q==-1:
      print("A sequência é uma PG alternante de razão %d",q) 
    if q==1:
      print("A sequência é uma PG Constante de razão %d",q)
      
    # se a sequencia for iniciada por números positivos
    if(sequencia[0]>0):
       #PG crescente => q>1
      if(q>1):
        print("A sequência é uma PG crescente para termos positivos de razão %d",q)
      #PG descrescente => 0<q<1
      if(q>0 and q<1):
        print("A sequência é uma PG decrescente para termos positivos de razão %d",q)
        
    # se a sequencia for iniciada por números negativos
    if sequencia[0]<0:
      #PG crescente pra termos negativos => 0<q<1
      if q>0 and q<1:
       print("A sequência é uma PG crescente para termos negativosd e razão %d",q)
    #PG descrescente pra termos negativos=> q<1
      elif q>1:
        print("A sequência é uma PG decrescente para termos negativos de razão %d",q)