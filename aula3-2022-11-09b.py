#criação de funções

preço = 1999.90

#Calcular 5% de imposto, guardar na variavel imposto e exibir na tela
imposto = preço * 0.05
print(imposto)

preço2 = 100
imposto2 = preço2 * 0.05
print(imposto2)

#Criar uma função calcular_imposto() que calcular um imposto de 5% e retorna a quem pediu...
#Isso é a declaração da função (Como ela funciona)
def calcular_imposto(preço_produto):
  imposto = preço_produto * 0.07
  return imposto 

#Aqui é o uso... aqui é imposto a calcular.. e exibir na tela
preço = 299
imposto = calcular_imposto(preço)
print(f"Esse aqui é com a função (7%): {imposto}")

#Explicação de variável local x global 
print(imposto) #???
preço_produto = 100
print(preço_produto) #???


#agora calcular imposto a alíquota agora é 7% 

valores = [1.99, 24.50, 78.27, 1515.5]
# se eu quiser calcular o imposto destes quatro valores... e exibir na tela assim: "O imposto de é ..."(10. preço, 20. imposto)
for valor in valores:
  print(f"0 imposto de {valor} é {calcular_imposto(valor)}")
           