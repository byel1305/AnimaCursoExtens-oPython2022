# comando input(): quero permitir que 
# o usuáriodigite algo...
nome = input("Digite seu nome: ")
# pede a idade para o usuário "Qual suaidade?"
idade = int(input("Digite sua idade: "))

# comando de saída..exibir na tela
print(f"Boa noite, seu nome é {nome}")
# exiba "Sua idade é ..."
print(f"Sua idade é {idade}")

#e se eu quisesse mostrar o DOBRO da  idade informada?
dobro = idade * 2
print("O dobro da idade informada é {}".format(dobro))

#Estrutura  condicional - o famoso "SE" (if)
#Se a pessoa  for maior de idade, mostrre"Voce é maior de idade, ótimo! já pode beber ou dirigir"
if idade >= 18:
  print("voce é  maior de idade, ótimo! já pode beber ou dirigir")
else:
  print("voce é xoven ainda, xoven ainda...")
  
#E se eu quissem perguntar o genero (M = Masculino e F = Ferminino)
#Mostre (...evoce também precisa/precisou prestar o serviço militar obrigatório)
genero = input("Informe ogenero M=Masculino, F=Feminino,O=Outros")
if idade >= 18 and genero == "M":
  print("... e voce também precisou prestar o serviço millitar obrigatório")






print("vai ser executada de qualquer jeito")