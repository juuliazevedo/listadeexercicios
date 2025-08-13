# Calculando a Média - 14

numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def media(lista):
  somadalista = sum(lista)
  media = somadalista/len(lista)
  return print(f"Total da lista: {somadalista}\nCálculo da média: {somadalista} / {len(lista)}\nResultado = {media}")

media(numeros)