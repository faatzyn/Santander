def exibir_poema(data_extenso, *args, **kwargs):
    # *args
    # Valores separados por virgula
    # Tudo que entrar como parametro, separado por virgula, sera um *args
    # Não pode ter chave
    texto = "\n".join(args)

    # kwargs
    # É um dict
    # Chave => Valor
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])

    # return
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

# exibir_poema("Terça, 05 de Setembro de 2023","Zen of Python", "Beatiful is better than ugly.", nome="Luiz",autor="Tim Peters", ano=1999)


# Parametros especiais
def parametros_especiais(pos1, pos2, /, pos_or_kwd, *, kw1, kw2):
    # Dessa maneira, eu obrigo os 2 primeiros (pos1, pos2) a ser por posição
    # Apos a /, pode ser por posição ou nomeado (pos_or_kwd)
    # Apos o * (kw1, kw2) apenas nomeados
    print(
        f"""
            Posição 1: {pos1}, Posição 2: {pos2}, Posição ou nomeado: {pos_or_kwd}
            Nomeado 1: {kw1}, Nomeado 2: {kw2}
        """
    )

# parametros_especiais("Primeiro", "Segundo", pos_or_kwd="Terceiro", kw1="Primeiro Nomeado", kw2="Segundo Nomeado")
# parametros_especiais("Primeiro", "Segundo", "Terceiro", kw1="Primeiro Nomeado", kw2="Segundo Nomeado")

def apenas_nomeados(*, nome, idade, afins):
    print(f"Nome: {nome}, Idade: {idade}, Afins: {afins}")

# apenas_nomeados(nome="Luiz", idade=28, afins="Estudante")

def hibrido(nome, sobrenome):
    print(f"{nome} {sobrenome}")

# hibrido("Luiz", "Assis")
# hibrido(nome="A", sobrenome="B")

def apenas_posicao(nome, sobrenome, /):
    print(f"{nome} {sobrenome}")

# apenas_posicao("L", "Z")
# apenas_posicao(nome="A", sobrenome="B") Erro

def somar(a,b):
    return a+b

def exibir_resultado(a, b, function):
    resultado = function(a,b)
    print(f"Resultado da operação: {resultado}")

# exibir_resultado(1,3,somar)

op = somar
print(op(1,23))