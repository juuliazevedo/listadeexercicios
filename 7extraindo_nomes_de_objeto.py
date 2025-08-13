# Extraindo Nomes de Objetos - 7

pessoas = [
    {"nome": "Thales", "profissão": "médico", "idade": 39},
    {"nome": "Carla", "profissão": "militar", "idade": 27},
    {"nome": "Valdez", "profissão": "cameraman", "idade": 28},
    {"nome": "Vitória", "profissão": "cantora", "idade": 30}
]

def extrair_nome(lista):
  lista_nomes = []
  for i in lista:
    lista_nomes.append(i["nome"])
  return lista_nomes

print(extrair_nome(pessoas))