# Tuplas
'''
Tuplas são quase idênticas as listas, com a única diferença que não podem ser modificadas, o valor inicial de uma tupla
ficará até o final do programa, seria basicamente um valor constante, ou seja, depois que você cria uma tupla, você não
pode alterar, adicionar ou remover elementos.

Para declararmos as tuplas no Python ao invés de colchetes [ ] (Usado nas listas), colocamos parênteses ( ).

Podemos “navegar” nas tuplas, assim como fazemos com as listas, passando o índice(posição) do item que desejamos buscar.
'''

# Por que usar Tuplas?
'''
Tuplas são úteis quando você precisa armazenar dados que não devem ser alterados. Alguns exemplos:
Data de nascimento
Coordenadas (x, y)
Informações fixas de configuração
Dados que você quer ler, não modificar
'''

# Como declarar uma Tupla?
tupla = ("Real Madrid", "Barcelona", "Arsenal", "Man City", "Man United")
print(tupla)

print("\n")

#Características das Tuplas:
'''
Característica       | Explicação
Imutável             | Não é possível adicionar, remover ou alterar elementos após a criação.
Indexada             | Você pode acessar os elementos pela posição (como em listas)
Aceita dados mistos  | Pode conter strings, inteiros, floats, booleans, etc.
Mais rápida          | A tupla ocupa menos memória e é mais rápida que a lista para leitura.
'''

# Exemplo prático:
dados = ("Michel", "22", "Desempregado", "Angolano")
print(dados[-1])
print(dados[1])

print("\n")

# Funções úteis com Tuplas
'''
Funções          | Descrição
len(tuplas)      | Retorna a quantidade de itens
tupla.count(x)   | Conta quantas vezes x aparece
tuplas.index(x)  | Retornar a posição da primeira ocorrência
'''
# Exemplos
cores = ("Azul", "Amarela", "Vermelho", "Laranja", "Branco", "Rosa", "Laranja", "Castanho", "Verde", "Laranja")
print(len(cores)) # 10 está função conta o quantos elementos existem dentro da tupla.
print(cores.count("Laranja")) # 3 quantas vezes um determinado valor aparece dentro da tupla.
print(cores.index("Branco")) # 4 retorna, ou menciona a posição onde o elemento está

# Observação importante
# Se você criar uma tupla com um único item, não esqueça da vírgula no final da código
tupla_simples = ("Angola",) # Correto
tupla_errada = ("Angola") # Isso é uma string, não uma tupla

print("\n")

print(tupla_errada)
print(tupla_simples)