# Encontrando o Segundo Maior Número - 3

numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def segundo_maior_numero(lista):
  maior = lista[0]
  segundo_maior = lista[0]
  for i in lista:
    if i > maior:
      segundo_maior = maior
      maior = i
    if i < maior and i > segundo_maior:
      segundo_maior = i
  return segundo_maior

print(segundo_maior_numero(numeros))