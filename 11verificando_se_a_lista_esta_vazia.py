# Verificando se a Lista está Vazia - 11

numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def lista_vazia(lista):
    if lista == []:
      return True
    else:
      return False

print(f"A lista é vazia? {lista_vazia(numeros)}")