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

