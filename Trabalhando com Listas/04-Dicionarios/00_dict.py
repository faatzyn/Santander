# DICT
# Conjunto ordenado de chave => valor
# Valores unicos por chave (Chave é imutável)

# Declaração
pessoa1 = {"nome": "Luiz", "idade": 32}
# ou
pessoa2 = dict(nome="Larissa", idade=27)

# Atribuindo
pessoa1["Telefone"] = "98816-6433"

contatos = {
    "luiz@gmail.com": {"nome":"Luiz", "idade":32},
    "lari@gmail.com": {"nome":"Larissa", "idade":27},
    "lucas@gmail.com": {"nome":"Lucas", "idade":9},
}

# print(contatos["luiz@gmail.com"]["nome"])

# Iterando um dict
# for chave, valor in contatos.items():
#     print(chave, valor)

# METODOS
# Copy
# Cria uma copia do dict, o que eu fizer na copia altera o principal
# Aquilo que eu alterar no principal, não altera na copia
contatos2 = contatos.copy()
# contatos2["pessoa"]["luiz@gmail.com"]["nome"] = 28
# print(contatos)
# print(contatos2)

# Clear
# Limpa o dict
# contatos.clear()
# print(contatos)

# FROMKEYS
# Cria chaves
# 1ª Situação, apenas cria a chave, sem valores
# contatos = dict.fromkeys(["nome","telefone","idade"])
# print(contatos)
# 2ª Situação, cria par de chave=>valor
# contatos = dict.fromkeys(["nome","telefone","idade"], "Teste")
# print(contatos)

# GET
# Segunda forma de acessar valores dentro de um dict
# contatos["chave"] # KeyError
# Caso não encontre, retorna a segunda opção, caso não passe a segunda opção, retorna none
# print(contatos.get("chave", {}))
# print(contatos.get("pessoa"))

# KEYS
# retorna apenas as chaves
# print(contatos.keys())

# POP
# Remove uma chave do seu dict
# Caso não encontre, retorna a segunda opção
# print(contatos.pop("chave", None))
# print(contatos.pop("luiz@gmail.com", {}))
# print(contatos.pop("nome", {}))
# print(contatos.pop("nome", {}))

# POPITEM
# Parecido ao POP, sem necessidade de indicar a chave
# Quando ficar vazio, retorna erro
# print(contatos.popitem())
# print(contatos.popitem())
# print(contatos.popitem())
# print(contatos.popitem()) #KeyError, por estar vazio

# SETDEFAULT
# Seto um atributo, caso não estiver no dict, eu seto um valor padrão, caso exista, não se altera
pessoa = {"nome":"luiz", "idade":32}
# print(pessoa.setdefault("nome", "apagar"))
# print(pessoa.setdefault("cidade", "Sorocaba"))

# UPDATE
# Permite atualizar o dict com outro dict
# print(contatos["luiz@gmail.com"])
contatos.update({"luiz@gmail.com":{"nome":"teste", "tel":"123"}})
# print(contatos["luiz@gmail.com"])

# VALUES
# Retorna todos os valores
# print(contatos.values())

# IN
# Verifica se existe a chave no dict
resultado = "luiz@gmail.com" in contatos
# print(resultado)
resultado_idade = "idade" in contatos["luiz@gmail.com"]
# print(resultado_idade)

# DEL
# Deleta um valor do dict
print(contatos)
del contatos["lari@gmail.com"]["idade"]
# print(contatos) # deletou a chave idade

