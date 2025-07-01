#Com este tema vamos aprender sobre dados ou conteúdo que podem ser armazenados dentro de uma variável.
#Tipos de Dados = Tipos de informações que uma variável pode armazenar/guardar.
#Tipos de dados suportados pelo Python
'''
Inteiros;
Float;
String;
'''

# Inteiros (int)
'''
São números negativos ou positivos, ou seja, números sem vírgula, números inteiros.
ex.: 123, 4, -2, -0, 13, -89
Usamos int quando estamos a contar algo (pessoas, livros, itens, páginas, tentativas, etc), ou seja, precisamos do valor exato
e inteiro, não faz sentido usar fração, tipo 3.2 pessoas/livros.
'''

# Float
'''
NÚmeros com casas decimais negativos ou positivos, ou seja, números com vírgula.
ex.: 1.85, 25.7, -87
Usamos os números com vírgula (ou ponto), porque eles representam valores fracionados ou medidas precisas, ou seja, quando
trabalhamos com medidas, valores monetários, ou precisamos de precisão. Cálculamos com ele percentagem, médias, distâncias, etc. 

'''

# String
'''
Usado para descrever textos, porém devem estar dentro de duplas aspas (" ") ou apas simples (' ').
ex.: "Michel", "Olá Mundo", "Ontem foi um dia muito triste porque ninguém se divertiu"
'''

# Boleano
'''
Além de números(int & float) e String, existe um terceiro tipo de dados em Python que não é exatamente um número ou uma
string, chamado de booleano (em homenagem a um matemático chamado George Boole), e pode ser um de dois valores: True ou False. 
'''

nome = "Michel" #string
idade = 24 #inteiro
altura = 1.85 #float
idade2 = 22
maior_de_idade = idade >= 18
print(f"Nome: {nome} \nIdade: {idade} \nAltura: {altura}")

if maior_de_idade:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")
print( idade > idade2) # True
print(nome.startswith("M")) # True
print(nome.endswith("l")) # True
print(nome.isnumeric()) # False
print(nome.isalpha()) # True


#Exemplo do que pode ser considerado como NÚMERO (int/float) e não Número (String).
#NÚMERO
'''
Exemplo   |   Tipo   | Explicação
1         |    int   | um número inteiro
1.1       |   float  | número decimal
12345.76  |   float  | decimal
-10       |    int   | inteiro negativo
.99       |   float  | decimal, mesmo sem o zero antes do ponto
'''

# NÃO NÚMERO
'''
Exemplo        | Explicação
192.168.1.1    | É um endereço de IP, separado por pontos. Não pode ser interpretado como número único
+244 929587744 | É um número de telefone com símbolos.
$100 OU 100KZ  | Tem símbolos de moeda, python entendi isso como textos
11.100.4       | Tem dois pontos decimais. Isso não é um número válido em python 
'''

# OBSERVAÇÃO
'''
Imagina que queremos escrever por exemplo "100Mil, 1Milhão, 1Mil ou Dez Mil e 20 centavos" como escrever no formato numérico?
Se a resposta foi "100.000  1.000.000  1.000   10.800,20" a resposta está errada. Porquê?
Porque não são considerados como números pelo python e sim strings (textos), por causa da formatação que usamos em português.
Entenda o porque: Em português, usamos ponto (.) para milhares e vírgula (,) para separar decimais. 
Mas em Python (e na maioria da linguagens): ponto (.) é usado como separador decimal e Milhares não tem ponto nem vírgula.
Como Python entende um número real corretamente:
Escrito em Português  | Forma correta em Python  |    Tipo
1.000                 |      1000                |    int
100.000               |      100000              |    int
1.000.000             |      1000000             |    int
10.800,20             |      10800.20            |    float
       

'''
print("\n")
# Funções e Módulos para Manipulação de String
'''
No Python existem várias funções e módulos para a manipulação de string. Uma função nada mais é que um bloco de código que é reutilizado, ou seja,
formas de escrever uma string, como se fosse ume editor de letras ou conteúdo da variável.
Um exemplo de uma função é a UPPER(), ela serve para colocar todas as letras em maiúsculo.
Se fizermos nome.upper() o retorno será "MICHEL". 
'''
nome = "michel"
print(nome.upper())

print("\n")
# Por que manipular strings?
'''
Por que eu me daria todo esse trabalho se eu simplesmente poderia fazer nome = "MICHEL" ?

Você só escreve desse jeito direto quando já o conhece e está fixo no código. Mas... e quando os dados vem de fora? De um usuário, de um formulário,
de um ficheiro CSV, ou de uma API?

Quando nós digitamos ( nome = "MICHEL") manualmente um dado conhecido, no código.
Ideal para testes simples ou valores fixos.

Mas na prática real (programas de verdade), os dados vêm como texto que precisamos organizar.
'''

# Por que manipular strings?
'''
Porque muitas vezes os dados chegam como textos, e precisamos:
Limpar
Corrigir
Separar
Unir
Substituir
Verificar partes do texto
'''
print("\n")
# Principais Funções do String
# 1- .upper() - Coloca tudo em  MAIÚSCULO
'''
Por que é útil:
Às vezes, padrões ou regras exigem que o texto fique todo em caixa alta (como nomes de produtos, siglas, ou códigos).

Onde se usa:
Impressão de documentos formais
Criação de identificadores únicos
Destaques visual em relatórios ou sistemas
'''
frase = "quando eu quero me conectar com alguém, eu me torno  o espelho dessa pessoa"
print(frase.upper()) # QUANDO EU QUERO ME CONECTAR COM ALGUÉM, EU ME TORNO O ESPELHO DESSA PESSOA

print("\n")

# 2-.lower - Coloca tudo em minúsculo
'''
O que faz:
Converte todas as letras de uma string para minúsculas, mesmo que estejam originalmente em maiúsculas.

Por que é útil:
Em muitas situações, você precisa comparar ou analisar palavras sem se importar com letras maiúsculas ou minúsculas. Exemplo:
quando o usuário digita "Luanda", "LUANDA" ou "luanda", todas devem ser reconhecidas como iguais.

Onde se usa:
Validação de login (e-mails/nomes de usuários)
Filtros de busca (para tornar a busca mais flexível)
Comparações sem erro por maiúsculas 
'''
frase1 = "QUANDO EU QUERO ME CONECTAR COM ALGUÉM, EU ME TORNO O ESPELHO DESSA PESSOA, PERMITO QUE ELE/A SE ENXERGUE EM MIM"
print(frase1.lower()) # quando eu quero me conectar com alguém, eu me torno o espelho dessa pessoa, permito que ele/a se enxergue em mim

print("\n")

# .lower() e .upper() - Padronização de textos
# Formação Profissional
'''
Ao comparar textos em sistemas, usamos .lower() ou .upper() para evitar erro por letras maiúsculas ou minúsculas.
'''
resposta = input("Deseja continuar? (sim/não)")
if resposta.lower() == "sim":
    print("Continuando...")

print("\n")

# 3- .title() - Coloca a primeira letra de cada palavra da string em maiúscula
'''
Por que é útil:
Ideal para títulos ou nomes completos. Garante que cada palavra importante apareça corretamente.

Onde se usa:
Títulos de artigo, livros ou seções
Formulários que capturam nome completo
Listagens organizadas
'''
frase2 = "A VIDA é um jogo de surpresa e NÃO JOGAR É ERRO DA NATUREZA, sei que essa frase não TEM SENTIDO."
print(frase2.title()) # A Vida É Um Jogo De Surpresa E Não Jogar É Erro Da Natureza, Sei Que Essa Não Tem Sentido

print("\n")

# 4- .strip() - Remove espaços em branco (ou outros caracteres indesejados) do início e fim da string
'''
Por que é útil:
Usuários muitas vezes digitam informações com espaços acidentais, que podem causar erros na hora de comparar, salvar ou processar dados.

Onde se usa:
Formulários online
Comparação de textos
Limpeza de dados importados
'''
frase3 = "      Quando eu quero que alguém me escute, eu começo ouvindo primeiro.        "
print(frase3.strip()) # "Quando eu quero que alguém me escute, eu começo ouvindo primeiro"

print("\n")

# 5- .replace("antigo", "novo") - Substitui uma parte específica da string por outra.
'''
Por que é útil:
Permite corrigir erros, traduzir palavras, limpar dados ou fazer substituições específicas no texto de forma dinâmica e automatizada.

Onde se usa:
Conversão de formatos de números
Troca de termos em relatórios
Substituição de gírias ou palavras proibidas
'''
valor = "10.800,20"
valor_corrigido = valor.replace(".", "").replace(",", ".")
print(valor_corrigido) # 10800.20

anime = "O meu anime preferido é Shingeki no Kyojin"
anime_corrigido = anime.replace("Shingeki no Kyojin", "One Piece.")
print(anime_corrigido) # O meu anime preferido é One Piece

'''
Nota de esclarecimento:
no primeiro exemplo, do número, utilizamos dois .replace e no segundo apenas um, isto porque,não p fazer várias substituição dentro de um
único replace(), porque o método replace só substitui uma coisa por vez.

valor_corrigido = valor.replace( Aqui removemos primeiro o ponto, ou seja, _old(mencionamos o que vamos remover) e new(removemos deixando em branco).
Isto é, 10.800,20 ficaria 10800,200).replace(Aqui trocamos a vírgula pelo ponto, ou seja, 10800,200 fica como 10800.200).

Então, podemos fazer várias substituições de uma vez desde que usarmos vários .replace().replace().replace() encadeado
No segundo exemplo fizemos apenas uma substituição.
'''
anime1 = ("Se eu pudesse categorizar os melhor animes que eu já assiste, a classificação seria (em ordem ascendente): Shingeki no Kyojin, "
          "Naruto, One Piece, Fairy Tail, Fire Force e Blue Lock")

anime1_corrigido = anime1.replace("Naruto", "The Promised Neverland") \
                         .replace("Fairy Tail", "Your Name") \
                         .replace("One Piece", "Ranking of Kings") \
                         .replace("Fire Force", "A Silent Voice") \
                         .replace("os melhor animes que eu já assiste", "os animes que eu gostei muito de assistir")
print(anime1_corrigido) # Se eu pudesse categorizar os animes que eu gostei muito de assistir, a classificação seria (em ordem ascendente): Shingeki no Kyojin,
                        # The Promised Neverland, Your Name, Ranking of Kings, A Silent Voice e Blue Lock
# Exite uma forma mais organizada de fazermos essas substituições
'''
Ideia Principal:
1- Criarmos um dicionário comos textos que queremos trocar
2- Usamos o loop for para aplicar cada substituição de forma automática
'''
texto = "Hoje é sexta feira e gostaria muito de sair com meus amigos para podermos beber algumas cervejas."

# Dicionário com os termos a substituir
substituicoes = {
"sair com meus amigos": "ficar em casa sozinho jogando PS4,",
    "para podermos beber": "isso seria mais divertido e relaxante do que tomar"
}

# Loop que aplica cada substituição no texto
for antigo, novo in substituicoes.items():
    texto = texto.replace(antigo, novo)
print(texto) # Hoje é sexta feira e gostaria muito de ficar em casa sozinho jogando PS4, isso seria mais divertido e relaxante do que tomar algumas cervejas

print("\n")

# 6- .split("separador") - Divide a string em partes, com base em um separador (espaço, vírgula, etc.) e devolve uma lista com as partes.
'''
Por que é útil:
Muitas vezes temos várias informações em uma só frase. Separar essas partes facilita o processamento e análise.

Onde se usa:
Processamento de arquivos CSV
Análise de comandos escritos pelo usuário
Separar nome e sobrenome, ou palavras-chaves
'''
frase4 = "Hoje será um dia muito calmo dado os acontecimento anteriores"
partes = frase4.split(" ")
print(partes) # ['Hoje', 'será', 'um', 'dia', 'muito', 'calmo', 'dado', 'os', 'acontecimento', 'anteriores']

print("\n")

# 7- .join(lista)- Junta elementos de uma lista em uma única string, usando um separador (como espaço, vírgula ou traço).
'''
Por que é útil:
Facilita a criação de frases ou arquivos de texto organizado, a partir de dados dividido.

Onde se usa:
Gerar frases automáticas
Exportar informações formatadas
Criar relatórios concatenando partes

'''
nomes = ['Arcanjo', 'Auriane', 'Hazael', 'Ariadina']
frase5 = ",".join(nomes)
print(frase5) # Arcanjo, Auriane, Hazael, Ariadina

print("\n")

# 8- in - Verificar se existe algo dentro da string
email = "etelvinojoaquim7@gmail.com"
print("@" in email) # True

print("\n")

# 9- .find("texto") - Procura a posição (índice) onde um trecho aparece na string. Se não encontrar, retorna -1.
'''
Por que é útil:
Ajuda a saber se uma palavra existe na frase e onde ela começa, antes de tomar decisões (como substituir, extrair, ou ignorar).

Onde se usa:
Verificação de comandos
Busca por palavras em arquivos
Análise de dados textuais
'''
mensagem = "Eu amo jogar PS4"
print(mensagem.find("PS4")) # 13
print(mensagem.find("amo")) # 3
print(mensagem.find("beber")) # -1

print("\n")

# 10 - len() - Mede quantos caracteres (letras, números, espaços, símbolos) existem dentro da string.
# Forma Profissional
'''
Por que é útil:
Ajuda a validar campos (como limites de senha), contar palavras ou caracteres.

Onde se usa:
Contar caracteres de um texto
Limites em formulários
Tamanho de senhas

Em sistemas reais (ex.: cadastro, senhas), usamos len() para garantir qualidade dos dados.
'''
if len(email) > 50:
    print("Email muito longo.")

print("\n")

# 11- .capitalize()
'''
O que faz:
Transforma apenas a primeira letra da frase em maiúscula e as demais em minúsculas.

Por que é útil:
Para exibir nomes e frases com aparência mais correta e elegante. Exemplo: "python é fácil" - "Python é fácil".

Onde se usa
Exibição de nomes
Títulos de seções em um sistema
Apresentação de repostas formatadas
'''
frase6 = "o mundo não é tão CRUEL quanDo VOCÊ PENSA ANTES DE AGIR."
frase6_renovada = frase6.capitalize()
print(frase6_renovada) # O mundo não é tão cruel quando você pensa antes de agir.

print("\n")

# 12- .count()
'''
O que faz:
Conta quantas vezes uma letra ou palavra aparece na string.

Por que é útil:
Permite detetar frequência de uso, repetições e analisar textos.

Onde se usa:
Estatísticas de palavras 
Controle de ocorrências (ex.: número de vezes que um nome aparece)
Verificação de repetição de caracteres em senhas 
'''
frutas = "maçã, morango, banana, ananás, laranja, morango, morango, laranja, laranja, morango, ananás"
quantidade1 = frutas.count("laranja")
quantidade2 = frutas.count("morango")
print(quantidade1) # 3
print(quantidade2) # 4

print("\n")

# 13- .startswith() / .endswith()
'''
O que fazem:
Verificam se a string começa ou termina com determinado conteúdo.

Por que são úteis:
São ótimos para validar formatos de dados, como verificar se um arquivo termina com .pdf ou se um código começa com uma letra específica.

Onde se usa:
Validação de e-mails ou links
Verificar extensões de arquivos
Identificar prefixos ou sufixos
'''
arquivo = "relatorio_final.pdf"
print(arquivo.startswith("relatorio")) # True
print(arquivo.endswith(".pdf")) # True
print(arquivo.endswith(".doc")) # False

arquivo2 = "Eu, Michel, quando estudava 3 classe, era apaixonada pela minha professora Marcia"
print(arquivo2.startswith("Eu")) # True
print(arquivo2.endswith("Marcia")) # True
print(arquivo2.endswith("Telma")) # False


print("\n")

# 14- .isnumeric(), .isalpha(), .isalnum
'''
O que fazem:
Verificam se a string contém apenas números, apenas letras, ou letras e números misturados, respetivamente.

Por que são úteis
Essas funções garantem que os dados inseridos seguem regras específicas.

Onde se usa:
Validação de códigos e senhas
Verificação de nomes e campos numéricos
Segurança e consistência de dados
'''
l = "929587744"
m = "Michel"
n = "Michel929587744"
o = "Michel24anos"
p = "Michel2000"
print(l.isnumeric()) # True - só números
print(m.isalpha()) # True - só letras
print(n.isalnum()) # True - letras e números
print(o.isalpha()) # False - contém letras e números
print(p.isnumeric()) # False - contém números e letras
# Em cada valor não pode ter símbolo ou espaço, apenas número ou letra

print("\n")

# 15- .zfill() e .rjust()
'''
O que fazem:
.zfill preenche com zeros à esquerda até atingir um tamanho desejado.
.rjust preenche com espaços (ou outro caractere) à esquerda até alcançar um tamanho.

Por que são úteis
São usados para formatar números ou strings e manter uma aparência uniforme em listas, arquivos, ou relatórios.

Onde se usam:
Código de produtos
Alinhamento de dados em tabelas
Impressão de boletos ou faturas
'''
cod = "50"
cod2 = "Amanhâ será um dia especial"
cod_reformado = cod.zfill(6) # Adiciona 0 à esquerda até ter 6 números no total
cod2_reformado = cod.rjust(6) # Adiciona espaço à esquerda até ter 6 caractere no total
print(cod_reformado)
print(cod2_reformado)

# 🔁 Inverter texto:
# texto[::-1]

# 🔼 Ordenar lista de números em ordem crescente:
# numeros.sort()numeros.sort()

#🔽 Ordenar lista de números em ordem decrescente:
# numeros.sort(reverse=True)
#Conclusão
'''
Essas funções tornam a manipulação de texto fácil, segura e poderosa. Elas são fundamentais em qualquer projeto real que envolva entrada,
validação ou formatação de textos, como:
Sistemas Web
Aplicações móveis
Sistemas bancários
Inteligência artificial
Leitura de arquivos
'''

# Módulo útil: textwrap (formata texto grande)
import textwrap
texto = "Eu Quero acabar de ler o livro V de Vingança, acredito que seja um livro bom de se ler."
print(textwrap.fill(texto, width=40))

mensagem1 = "      Bem-Vindo, Michel!  "
mensagem1 = mensagem1.strip()
print(mensagem1.upper()) # Bem-Vindo, Michel!



