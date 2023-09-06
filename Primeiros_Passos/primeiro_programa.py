b = 10
c = 20
LUIZ = 'LUIZ'
LUIZ = 'RENAN' # SOBRESCREVE A CONSTANTE
# print(LUIZ)
# dir() -> Mostra o escopo local
# dir(numero) -> mostra todo o escopo do número, se int, mostra tudo da classe int e assim por diante
# help() exibe um menu para eu pedir ajuda sobre agora, Ex.: str, mostra todos os métodos da classe str

# nome = input("Informe seu nome: ")
# idade = input("Informe sua idade: ")
# print(nome, idade)
# Variacoes de print
# end -> entra no final do print
# print(nome, idade, end="... \n\n")
# sep -> Separa as variaveis dentro do print
# print(nome, idade, sep="    ", end=" ......\n")

# Operadores aritmeticos
# Adicao -> 1 + 14 = 15
# Subtracao -> 2 - 1 = 1
# Divisao inteira -> 5 / 2 = 2
# Divisao -> 5 / 2 = 2.5
# Modulo = 10 % 3 = 1 (Pega o resto)
# Multiplicacao = 5 * 2 = 10
# Exponencial = 5 ** 2 = 25

# Operadores de Comparacao
# Igualdade ==
# Diferenca !=
# Maior > ou maior igual >=
# Menos < ou menor igual <=

# Operadores de Atribuicao
# +=   -=    *=   /=    //=   %=   **=

# Operadores Logicos
# and --- or --- not (!) --- 

# Operador de Identidade
curso = "Curso Python"
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso # verifica a mesma referencia na memória
# True, pois o valor dentro da variável curso, é o que está dentro da nome_curso
# Ambas as variáveis apontam para a mesma referencia de memoria
# print(curso is nome_curso, nome_curso is curso)
curso is not nome_curso # Verifica a referencia de memória das variaveis são diferentes
# False, pois apontado para o mesmo espaço de memória
# print(curso is not nome_curso, nome_curso is not curso)

# Operador associativo
curso = "Curso de Python"
frutas = ["A", "B", "C"]
# print("Python" in curso) # True, pois achou no texto na variavel
# print("A" in frutas) # True, pois achou no texto na variavel
# print("D" not in frutas) # True, pois nao era para achar

# Estruturas de loop
# texto = "123"
# for i in texto:
#     print(i)
# else: # Passo que executa ao final do for
#     print('fim')

# for i in range(6):
#     print(i)
# else:
#     print('fim')

# range(inicio, fim, passo), fim e passo são opcionais
# for i in range(0, 100, 10):
#     print(i)
# else:
#     print('fim')

# opcao = -1
# while (opcao != 0):
#     opcao = int(input("Digite 0 para sair: "))
#     if opcao != 0:
#         print("Não saiiii \n")
#     else:
#         print("Agora sim Estou saindo.")

while True:
    opcao = int(input("Digite 0 para sair: "))
    if opcao != 0:
        print("Não saiiii \n")
    else:
        print("Agora sim Estou saindo.")
        break