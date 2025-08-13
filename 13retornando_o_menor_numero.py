# Retornando o Menor Número - 13

numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def menor_numero(lista):
  menor = lista[0]
  for posição in lista:
    if posição < menor:
      menor = posição
  return menor

print(menor_numero(numeros))