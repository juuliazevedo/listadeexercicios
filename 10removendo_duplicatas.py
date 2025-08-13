# Removendo Duplicatas - 10

numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def remove_duplicata(lista):
  lista_semduplicata = []
  for i in lista:
    if i not in lista_semduplicata:
      lista_semduplicata.append(i)
  return lista_semduplicata

print(remove_duplicata(numeros))