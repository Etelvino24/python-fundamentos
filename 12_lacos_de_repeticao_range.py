# 🔎 Pergunta
'''
Então, range é apenas para números?
E
Se por exemplo tivermos uma listagens de itens númerados dentro de uma lista, dicionário ou tuplas por exemplo e
queremos acessar, apesar de serem nomes de coisas ou descrição de alguma coisa mas estão organizados por números,
em ordem, podemos acessar com range()?
'''

# ✅ 1. Sim, range() é apenas para números
# A função range() só gera números inteiros.
# Ela não serve para gerar palavras, objetos, textos ou outros tipos de dados diretamente. Mas... 👇

#✅ 2. Podemos usar range() para acessar elementos de listas, tuplas ou dicionários organizados por posição
# Mesmo que os itens sejam nomes, descrições ou qualquer conteúdo, se eles estiverem dentro de uma estrutura como lista,
# tupla ou dicionário, e você quiser acessar por índice (posição), então sim, o range() pode te ajudar.

# 📌 Exemplo com uma lista:
compras = ["Arroz", "Feijão", "Massa", "Açúcar"]

for i in range(len(compras)):  # range(4) → 0, 1, 2, 3
    print(f"{i+1} - {compras[i]}")

# 📤 Saída:
# 1 - Arroz
# 2 - Feijão
# 3 - Massa
# 4 - Açúcar
# Aqui, mesmo sendo nomes de coisas, como estão em uma lista (e listas têm posições numéricas), o range() nos ajuda a
# acessar cada uma com índice.

print("\n")

# 📌 Exemplo com uma tupla:
filmes = ("Matrix", "Titanic", "Vingadores")

for i in range(len(filmes)):
    print(f"Filme {i+1}: {filmes[i]}")

print("\n")

# 📌 E com dicionário?
# O range() não é o mais comum com dicionários, pois dicionários não usam posições numéricas, mas sim chaves.
# Mas veja uma forma possível se quisermos usar range() com as chaves:

dados = {
    "nome": "Etelvino",
    "idade": 24,
    "cidade": "Luanda"
}

chaves = list(dados.keys())  # transforma as chaves em lista

for i in range(len(chaves)):
    print(f"{chaves[i]}: {dados[chaves[i]]}")



# ✅ Conclusão:
'''
| Situação                                  | Usar `range()`? |
| ----------------------------------------- | --------------- |
| Precisa de uma sequência de números       | ✅ Sim           |
| Quer repetir algo X vezes                 | ✅ Sim           |
| Está acessando índice de lista/tupla      | ✅ Sim           |
| Está lidando com nomes/textos diretamente | ❌ Não           |

'''

print("\n")

# 📌 range(start, end, step)
for numero in range(4,10,2,):
    print(numero)

# A função range() em Python só aceita até 3 argumentos, e cada um tem um papel muito específico:
# 📌 range(início, fim, passo)
'''
| Posição | Significado        | Exemplo              |
| ------- | ------------------ | -------------------- |
| 1º      | Início (inclusivo) | `4` (começa no 4)    |
| 2º      | Fim (exclusivo)    | `10` (vai até 9)     |
| 3º      | Passo (intervalo)  | `2` (pula de 2 em 2) |
'''

# 📌 Exemplos:
for animes in range(5):
    print(animes)

print("\n")

for musica in range(2,6):
    print(musica)

print("\n")

for filmes in range (1,11,2):
    print(filmes)

print("\n")

# 🔎 Pergunta?
# 📌 for chave, valor in pessoa.items():
# Então, para o for antes de in, podemos adicionar mais de duas descrições?

# 📌 Sim, você pode adicionar mais de uma variável antes do in no for, mas isso depende do que está sendo iterado.
# Vamos entender de forma clara e didática:

# ✅ Como funciona o for com múltiplas variáveis antes do in:
# O Python permite isso quando o item iterado retorna múltiplos valores ao mesmo tempo (como uma tupla com dois, três ou
# mais valores). Vamos ver os casos:

# 🧠 1. Dicionários com .items()
pessoa = {"nome": "Etelvino", "idade": 24}

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

# ✅ Aqui, .items() retorna pares (chave, valor) — uma tupla com 2 elementos — por isso usamos for chave, valor in.

print("\n")

# 🧠 2. Listas de tuplas com 3 ou mais elementos
dados = [("João", 25, "Masculino"), ("Maria", 30, "Feminino")]

for nome, idade, sexo in dados:
    print(f"{nome} tem {idade} anos e é do sexo {sexo}.")

# ✅ Como cada item da lista é uma tupla com 3 valores, usamos três variáveis.

print("\n")

# 🧠 3. Enumerate com listas
nomes = ["Etelvino", "Ana", "Carlos"]

for indice, nome in enumerate(nomes):
    print(f"{indice}: {nome}")

# ✅ enumerate(nomes) retorna (índice, valor), então usamos duas variáveis.

# 🔢 O que é enumerate()?
# É uma função embutida (built-in) do Python usada para percorrer uma lista (ou outro iterável) e obter, ao mesmo tempo,
# o índice (posição) e o valor de cada item.

# 🧠 Por que usamos enumerate()?
'''
Imagine que você quer imprimir todos os itens de uma lista e mostrar qual é a posição de cada um.
Sem enumerate(), você teria que usar o range() junto com len(), o que é mais trabalhoso.
Com enumerate(), fica mais simples, limpo e legível.
'''
# 📌 Sintaxe do enumerate:
# for índice, valor in enumerate(lista):


#❗ Quando NÃO dá pra usar várias variáveis?
'''
Se estiver iterando algo que devolve apenas um valor por vez, como uma lista simples:

nomes = ["Etelvino", "Maria", "João"]

# ERRADO:
for nome, idade in nomes:
    print(nome, idade)

❌ Vai dar erro, porque nomes só tem um valor por vez (só o nome).
'''

#✅ Resumo prático
'''
| Tipo de estrutura                   | Pode usar múltiplas variáveis no `for`? | Exemplo                          |
| ----------------------------------- | --------------------------------------- | -------------------------------- |
| Dicionário com `.items()`           | ✅ Sim (chave, valor)                    | `for k, v in dicionario.items()` |
| Lista de tuplas (2 ou mais valores) | ✅ Sim (desempacotamento)                | `for a, b, c in lista`           |
| `enumerate(lista)`                  | ✅ Sim (índice, valor)                   | `for i, v in enumerate(lista)`   |
| Lista simples (strings, ints...)    | ❌ Não                                   | Apenas `for item in lista`       |
'''

# 🔎 Agora vamos entender sobre "desempacotamento"!
# 📌 Pergunta?
# dados = [("João", 25, "Masculino"), ("Maria", 30, "Feminino")]
# for nome, idade, sexo in dados:
# como o programa vai entender que nome, idade e sexo fazem parte dos dados, já que não foram definidas como variáveis e
# os valores como João, 25, Masculino, não estão diretamente ligados com essas variáveis?

# 🔍 Situação:
'''
dados = [("João", 25, "Masculino"), ("Maria", 30, "Feminino")]

for nome, idade, sexo in dados:
    print(f"{nome} tem {idade} anos e é do sexo {sexo}.")
'''

# 🧠 Como o Python entende isso?
# 1- dados é uma lista de tuplas.
'''
[
    ("João", 25, "Masculino"),
    ("Maria", 30, "Feminino")
]
'''
# Ou seja, cada item da lista é uma tupla com 3 valores.

# 2- No for, ao fazer:
'''
for nome, idade, sexo in dados:
'''

# O Python pega um item por vez da lista — ou seja, uma tupla com 3 valores — e desempacota automaticamente nos nomes
# das variáveis que você colocou:
# 💡 "João" vai para nome
# 💡 25 vai para idade
# 💡 "Masculino" vai para sexo

# 🧯Mas como ele sabe que João é nome, 25 é idade, etc?
# Na verdade, ele não sabe nem se importa com o “significado” do nome das variáveis.
# O Python só segue a ordem dos valores da tupla!
# 📦 Ele apenas “abre o pacote” e distribui:
# A correspondência é por posição:
# 💡 1º valor da tupla → 1ª variável
# 💡 2º valor da tupla → 2ª variável
# 💡 3º valor da tupla → 3ª variável


