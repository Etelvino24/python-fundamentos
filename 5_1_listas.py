# Lista em Python
'''
Como o próprio nome diz lista é um conjunto de elementos juntos, por exemplo: imagina que você vai no mercado, e para
lembrar de todas as coisas que precisa comprar, você decide anotar em uma folha de caderno cada item.

Você começa escrevendo a partir da primeira linha da folha, né?

Suponhamos que em sua lista você insere:
Ovos
Arroz
Massa
Detergente
Açúcar
'''

# Características importantes das listas:
'''
Aceitam vários tipos de dados (números, textos, booleanos... tudo junto se quiser).
A ordem importam: o primeiro item está na posição 0, o segundo na posição 1, e assim por diante.
São mutáveis: você pode adicionar, mudar ou remover elementos depois que a lista for criada.
'''

# Acessando elementos da lista
'''
Podemos referenciar posições para busca de um elemento dentro de uma lista, voltando no exemplo do mercado, se a
prateleira de açúcar(último item) está perto da prateleira de ovos (primeiro item), podemos pular direto para a última
posição e buscarmos o açúcar, cor reto?

Da mesma forma ocorre com Python, para buscar um elemento em uma lista, usamos os colchetes [ ] passamos a posição que
queremos buscar, que sempre é um número inteiro.

Também no Python, podemos referenciar um número inteiro negativo para nossa lista, desta forma ela retorna para o final
da lista.
Exemplo: lista = [-1]
Ou seja, quando colocamos um número negativo, a lista é lida de trás para frente.
'''

# Listas
compras = ["Ovos", "Arroz", "Massa", "Detergente", "Açúcar"]
nomes = ["Michel", "Arcanjo", "Auriane", "Manuel," "Domingas"]
idades = ["24", "11", "8", "63", "52"]
print(compras [4])
print(nomes)
print(idades[-3])

print("\n")

# Funções úteis com listas
'''
Função              | O que faz
append()            | Adiciona um item no final
insert(pos, valor)  | Insere em uma posição
remove(valor)       | Remove um item específico
pop()               | Remove o último item
len()               | Retorna o tamanho da lista
sort()              | Ordena a lista
reverse()           | Inverte a ordem
clear()             | Apaga todos os itens
'''
animes = ["Naruto", "One Piece", "Blue Lock", "Your Name", "A silent Voice", "Bersek", "Shingeki no Kyojin", "The Promised Neverland"]
animes.append("Spy x Family")
animes.sort() # letras ordem em ordem alfabética e número em ordem numérica e em ordem decrescente usamos o .short(reverse=True)
animes.insert(5, "Haikyuu")
animes.pop(1) # Pop remove o último item, mas também podemos direcionar para tornar mais específico o que queremos remover
print(len(animes))
print(animes)

for item in animes: # Para colocar a lista em ordem horizontal
    print(item)

# outra formas (sem o for, usando o join e \n)
# print("\n".join(animes))

