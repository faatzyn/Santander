# Conjunto é uma coleção de objetos que contem objtos unicos (não se repetem)
conjunto = set([1,2,2,2,3]) # Ele apaga os duplicados
# print(conjunto)
frutas = set("abacaxi") # Lembrando que o set não mostra exatamente como foi criado (não ordena)
# print(frutas)
nome = {"Luiz","Assis"}
# print(nome)

# Para acessar os dados, é necessário converter o conjunto para uma lista
numeros = list(conjunto)
# print(numeros[0])

# Para acessar por for, funciona
# for f in frutas:
    # print(f)

conjunto_a = {1,2,3}
conjunto_b = {3,4}

# UNION
novo_conjunto = conjunto_a.union(conjunto_b)
# print(novo_conjunto)

# INTERSECTION
# É a parte do conjunto em que são iguais
conjunto_intersection = conjunto_a.intersection(conjunto_b)
# print(conjunto_intersection, conjunto_a, conjunto_b)

# DIFFERENCE
# Tudo que tenho num conjunto que não está no outro
conjunto_diff = conjunto_a.difference(conjunto_b)
# print(conjunto_diff)

# SYMMETRIC_DIFFERENCE
# Tudo que não tem no outro conjunto (não se repete)
conjunto_sym_diff = conjunto_a.symmetric_difference(conjunto_b)
# print(conjunto_sym_diff)

# ISSUBSET
# Verifica se um conjunto é subconjunto de outro
# retorna bool
conjunto_issubset = conjunto_a.issubset(conjunto_b)
# print(conjunto_issubset)

# ISSUPERSET
# Verifica se o proximo conjunto pertence ao primeiro
# retorna bool
conjunto_issuperset = conjunto_a.issuperset(conjunto_b)
# print(conjunto_issuperset)

# ISDISJOINT
# Conjuntos onde não se tocam
# retorna bool
conjunto_isdisjoint = conjunto_a.isdisjoint(conjunto_b)
# print(conjunto_isdisjoint)

# ADD
# Posso passar um elemento, caso não exista, ele é adicionado
conjunto_a.add(6)
# print(conjunto_a)

# CLEAR
# Limpa o conjunto
# COPY -> Copia o conjunto
conjunto_clear = conjunto_a.copy()
# print(conjunto_clear)
conjunto_clear.clear()
# print(conjunto_clear)

# DISCARD
# Descarta um valor do conjunto
conjunto_a.discard(6)
# print(conjunto_a)

# POP
# Remove o primeiro elemento do conjunto, caso não passe a posição
conjunto_a = conjunto_a.union([7,8])
# print(conjunto_a)
# print(conjunto_a.pop())

# REMOVE
# Muito parecido com o DISCARD, contudo se passar um valor que não exista, gera uma exceção, o DISCARD não gera
conjunto_a = conjunto_a.union([1,4,5])
# print(conjunto_a)
# print(conjunto_a.remove(1))
# print(conjunto_a)

# LEN
# Retorna o tamanho do conjunto
# print(len(conjunto_a))

# IN
# Verifica se existe o valor no conjunto
# print(1 in conjunto_a)

