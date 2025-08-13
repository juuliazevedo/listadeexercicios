# Juntando Duas Listas - 12

natureza = ["rio", "floresta", "leão", "montanha", "oceano", "estrela", "vento", "cachoeira", "lua", "girassol"]
tecnologia = ["algoritmo", "API", "blockchain", "código", "software", "nuvem", "hardware", "interface", "pixel", "servidor"]

def concatenação_lista(lista1,lista2):
  lista_concatenada = lista1 + lista2
  return lista_concatenada

print(concatenação_lista(natureza,tecnologia))