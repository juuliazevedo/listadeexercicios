# Somando os Valores da Lista - 8

numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

def somador_lista(lista):
  soma = 0
  for i in lista:
    soma += i
  return soma

print(somador_lista(numeros))