#Pede o nome do aluno e sua nota (de 0 a 10 ) e, se ele tirou nota 10, mostra "{nome}, Voce é bichão, mesmo"
nome = input("Informe seu nome:")
nota = float(input("Digite sua nota: "))

if (nota == 10):
  print(f"{nome}, voce é bichão, mesmo...")
elif(nota >= 6 and nota < 10):
  print(f"{nome}, bom trabalho")
else:# ésempre automaticamente o  que as duas condiições não tratamento
  print("Burro, não tirou dez...")


