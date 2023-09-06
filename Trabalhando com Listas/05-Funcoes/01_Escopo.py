# Escopo Local -> Feito dentro de um escopo mais interno
# Assim que termina o escopo, as variaveis dentro dela são perdidas

# Escopo Global -> Tudo além do escopo local
# Declarado no escopo global

salario = 2000 #  Escopo global, pois está na raiz do programa

def salario_bonus(bonus):
    global salario # Utiliza a variavel global (fora desse escopo)
    global lista
    salario += bonus

    # Crio uma cópia, onde posso alterar sem prejudicar a variavel global'
    lista2 = lista.copy()
    lista2.append(salario)

    print(lista2)
    return salario

lista = [1]
print(salario_bonus(100), lista)