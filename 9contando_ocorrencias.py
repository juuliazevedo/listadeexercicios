# Contando Ocorrências - 9

numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
num = int(input("Digite um valor: "))

def conta_aparições(lista,valor):
  cont= 0
  for i in lista:
    if i == valor:
      cont += 1
  return cont

print(f"Aparições na lista: {conta_aparições(numeros,num)}")