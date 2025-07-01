# Laços e Repetição
'''
Agora aprenderemos um conceito muito interessante e muito usado em qualquer linguagem de programação chamado LAÇOS
DE REPETIÇÃO.
'''

# 🧠 O que são Laços de Repetição?
'''
Laços de repetição são estruturas que permitem repetir uma ou mais instruções de forma automática, até que uma 
condição seja satisfeita.

É como dizer para o computador:

"Enquanto algo for verdadeiro, continue fazendo isso"
ou
"Para cada item nessa lista, faça tal coisa".
'''

# 🔎 Por que Usamos?
'''
Imagine se você tivesse que escrever o comando print("Olá!") cem vezes para dar bom dia a cem pessoas...

Com um laço, você escreve uma única vez e manda o computador 100 vezes por você.
📌 Evita Código repetitivo
📌 Facilita alterações e manutenção
📌 Torna o programa mais inteligente e adaptável
'''

# 🎯 Quando usamos?
'''
Usamos laços de repetição sempre que:
•	Precisamos executar ações mais de uma vez
•	Temos que percorrer listas (ex: nomes, números, produtos)
•	Queremos esperar uma condição acontecer (ex: o usuário digitar certo)
•	Desejamos automatizar tarefas rotineiras
'''

# 🛠️ Tipos de laços em Python
'''
Tipo de Laço | Quando Usar?             | Explicação
while	     | Condições indefinidas	| Enquanto a condição for verdadeira, continua repetindo
for	         | Situações definidas      | Para cada item em uma sequência ou intervalo, executa
'''

# 📘 Analogia simples:
'''
Imagine um relógio com alarme que só para de tocar quando você acorda. Isso é um while.
Agora, imagine que você quer beber 5 copos de água por dia. Você faz isso 5 vezes, independentemente de qualquer coisa. 
Isso é um for.
'''

#🧪 Cenário real: Lista de compras
'''
Imagine que você tem uma lista de compras com vários itens e quer exibir um por um. Como já sabemos exatamente quantos 
itens existem, o for é ideal aqui.
'''

lista_compras = ["Arroz", "Feijão", "Óleo", "Sabão", "Leite"]
# 📌 Exemplo com for:
for item in lista_compras:
    print("Você precisa comprar:", item)

print("\n")

# 🧠 O que está acontecendo?
'''
O for pega cada item da lista e guarda temporariamente na variável item.
Em cada volta do laço, ele executa o print() com o valor atual de item.
Quando acaba a lista, o laço também termina.
'''

# 🧰 Outros usos do for
# Se quiser fazer algo um número fixo de vezes, também pode usar for com a função range():

# 📌 Exemplo com range():
for numero in range(1, 6):  # Vai de 1 até 5
    print("Esta é a repetição de número:", numero)

# ✅ Quando usar o for?
# 📌 Quando sabemos quantas vezes a ação será repetida.
# 📌 Quando estamos percorrendo listas, strings, dicionários ou usando range().
# 📌 Quando queremos fazer ações organizadas em sequência (ex: imprimir uma tabela, listar nomes, contar de 1 a 10, etc.).

print("\n")

#🧪 Cenário real: Senha correta
# Imagine que você tem um sistema que só deixa o usuário entrar quando digita a senha certa. Você não sabe quantas
# tentativas ele vai precisar. Isso é perfeito para usar o while.

# 📌 Exemplo com while:
senha_correta = "python123"
senha_digitada = input("Digite a senha: ")

while senha_digitada != senha_correta:
    print("Senha incorreta. Tente novamente.")
    senha_digitada = input("Digite a senha: ")

print("Acesso permitido! Bem-vindo.")

# 🧠 O que está acontecendo?
# 📌 O programa pede a senha.
# 📌 Se estiver errada, ele repete o pedido infinitamente até o usuário digitar corretamente.
# 📌 Quando a senha está certa, o laço para automaticamente e o acesso é concedido.

# ✅ Quando usar o while?
# 📌 Quando não sabemos quantas vezes a repetição acontecerá.
# 📌 Quando dependemos de uma condição externa (como entrada do usuário).
# 📌Quando queremos validar dados, como idade, senha, escolha de opções, etc.