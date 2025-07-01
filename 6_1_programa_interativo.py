# Programa Interativo em Python
'''
Um programa interativo é aquele que pede informações ao usuário usando a função input() e responde com base nesses dados
usando print(), ou seja, é um programa interativo porque interagi com o usuário.
'''

# Por que usar?
'''
Permite que o usuário participe
Torna o programa mais dinâmico
É o início para criar sistemas reais 
'''
# Estrutura básica
# Cadastro Simples
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
print(f"Olá, {nome}! Você tem {idade} anos.")
# No terminal, é onde vais digitar os seus dados e apertar enter para cada pedido.
# input() Pede uma informação ao usuário;
# print() Exibe a resposta no terminal;
# f" " Formata  a mensagem com os dados digitados
'''
Resumo:
O texto dento do input("...") é so uma mensagem para o usuário saber o que digitar.
O valor qu será armazenado na variável é o que o usuário digitar manualmente no terminal
'''
# Erro comum:
# Nãos se deve escrever o valor direto na mensagem do input("..."), como:
# nome = input("Digite seu nome: Michel")
# Isso faz parecer que o nome já foi definido, mas não é o caso.
# O input("...") só exibe o texto, e espera que o usuário DIGITE o valor no terminal.

