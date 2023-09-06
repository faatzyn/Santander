# TUPLAS - Seus valores são IMUTAVEIS - Muita similaridade com listas
frutas = ("a","b","c",) # Sempre bom colocar uma virgula no final
letras = tuple("LuizAssis")
numeros = tuple([1,2,3,4])
pais = ("brasil",)

# print(frutas)
# Tupla é uma sequencia
# print(frutas[0]) # Tem as mesmas caractertisticas de uma lista
# print(frutas[-1]) #
# print(frutas[::-1]) #

matriz = (
    (1,'a',2),
    ('b',3,4),
    (6,5,'c'),
)

# USA-SE A TUPLA QUANDO VC NÃO QUER QUE OS VALORES SEJAM ALTERADOS
print(matriz[::-1])