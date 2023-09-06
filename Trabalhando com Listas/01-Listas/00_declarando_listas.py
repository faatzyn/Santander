# Lista, funciona como se fosse um array, podendo trabalhar com todos os tipos de variáveis
# Lista é uma sequencia
frutas = [] # Lista Vazia
frutas = ["Maça", "Banana", "Mamão"]
letras = list("Luiz") # Cria uma lista com 4 objetos, ["L","u","i","z"]

# print(letras[-1]) # Acess o ultimo elemento
# print(letras)

# A Lista é um objeto que pode adicionar outras listas
# Lista Aninhada o nome disso
# matriz = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,"z"]
# ]

# print(matriz[0]) # Acessa o primeiro objeto
# print(matriz[-1]) # Acessa o ultimo objeto
# print(matriz[-1][-1]) # Acessa o ultimo objeto e o ultimo elemento

# FATIAMENTO
# fatiamento = list("LuizAssis")
# print(fatiamento)
# print(fatiamento[0:4]) # Coemçando da 0, anda 4
# print(fatiamento[0::3]) # Coemçando da 0, ate o fim, de 3 em 3
# print(fatiamento[::-1]) # Espelhando a string

# PERCORRER COM FOR
# carros = ["gol","celta","palio"]
# for i in carros:
#     print(i)

numeros = list(range(10))
pares1 = []
# print(numeros, pares)
for i in numeros:
    if i%2 == 0:
        pares1.append(i)
# print(pares)
# Percorrer de maneira mais performatica
pares2 = []
# print(pares2)
# Esse trecho tem uma performance maior
pares2 = [numero for numero in numeros if numero%2 == 0]
# print(pares2)
# Sem o if (filtro)
todos_aos_quadrados = [numero**2 for numero in numeros]
# print(todos_aos_quadrados)

# METODOS da classe LIST
lista = [1,3,3,4,5,6,67,"sd"]

# COPY
lista2 = lista.copy() # Copia a lista, tendo referencia distinta
# sendo assim o que faço em uma não ocorre na outra

# CLEAR
lista.clear() # Limpa a lista
# print(lista, lista2)
lista2.append('zzzz') # Adiciona no final da lista
# print(lista, lista2)

# COUNT
# print(lista2.count(3)) # Retorna o numero de ocorrencias (qtde)

# EXTEND
lista3 = [1,1,1,1,1]
lista2.extend(lista3) # Add uma nova lista (une duas listas)
# print(lista2) 

# INDEX
lista2.index("sd") # Retorna a posição onde está a primeira ocorrencia valor procurado
# print(lista2.index("sd"))

# POP
# print(lista2)
lista2.pop() # Remove o ultimo elemento
# print(lista2)
lista2.pop(7) # Remove o elemento 7
# print(lista2)

# REMOVE
# print(lista2)
lista2.remove("zzzz") # Remove a partir do valor, Remove apenas a primeira ocorrencia
# print(lista2)

# REVERSE
lista2.reverse() # INVERTE A LISTA
# print(lista2)

# SORT
lista2.sort() # Reordena em ordem crescente
# print(lista2)
lista4 = ['ab','cff','cd','dg','easdaw','fdfgftdasdf']
# print(lista4)
lista4.sort() # Reordena em ordem alfabetica. OBS.: Não tem como misturar int e str
# print(lista4)
lista4.sort(reverse=True) # Reordena ao contrário
# print(lista4)
# Reordena ao contrario, pelo tamanha da string (da maior para a menor)
lista4.sort(key=lambda x:len(x), reverse=True)
# print(lista4)

# LEN
len(lista4) # Retorna o tamanho da lista, ou string
# print(len(lista4))

# SORTED
# Ordenar iteráveis
sorted(lista4, key=lambda x: len(x), reverse=True)
print(lista4)
