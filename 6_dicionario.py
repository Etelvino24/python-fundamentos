# Dicionário
'''
Um dicionário em Python é uma estrutura de dados que serve para armazenar informações com "rótulos"

Esses rótulos são chamados de chaves (keys) e os dados que estão ligados a essas chaves são os valores (values).

É como um dicionário real:
A palavra é a chave
A Definição da palavra é o valor
'''

# Exemplo
pessoa = {
     "nome": "Epifânia Joaquim", # "nome" é a chave e "Epifânia Joaquim" é o valor
     "idade": 33,  # "idade" é a chave e "33" é o valor
     "bilhete": "0030026132LA036", # O mesmo princípio para o restante
     "residência": "Zango III, Viana",
     "naturalidade": "Cazenga",
     "província": "Luanda",
     "sexo": "Feminino",
     "altura": 1.85,
     "estado civil": "Casada",
     "telefone": 929587744
}

# Como acessar a todos os dados
print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["bilhete"])
print(pessoa["residência"])
print(pessoa["naturalidade"])
print(pessoa["província"])
print(pessoa["sexo"])
print(pessoa["altura"])
print(pessoa["estado civil"])
print(pessoa["telefone"])

print("\n")

# Podemos também
# Adicionar um novo item:
pessoa["profissão"] = "Professora"

# Alterar um valor
pessoa["altura"] = 1.75

# Remover um item:
del pessoa["bilhete"]

# Ver todas as chaves:
print(pessoa.keys())

print("\n")

# ver todos os valores
print(pessoa.values())

print("\n")

# Ver tudo, chave e valores
print(pessoa.items())

print("\n")

# ver tudo na Horizontal
for chave, valor in pessoa.items():
     print(f"{chave}: {valor}")

print("\n")

carro = {
     "marca": "Toyota",
     "modelo": "Corolla",
     "ano": "2022",
     "cor": "vermelha"
}

for chave, valor in carro.items():
     print(f"{chave}: {valor}")

