#Vamos aprender sobre Variáveis e Operadores.

#VARIÁVEIS
'''
Variáveis são como métodos de armazenamento de valores (informação) dentro de um programa, ou seja, elas armazenam conteúdo/informação. 
Usamos Variáveis para guardar valores temporariamente.
valores (informação/conteúdo) que pretendemos utilizar. Para guardar uma informação primeiramente definimos as Variáveis, depois utilizamos
um símbolo para atribuir o valor ou a informação/conteúdo e por fim descrevemos a informação que queremos guardar.
exemplo prático.: nome = "Michel";
nome: variável;
= : sinal de atribuição, ou seja, declarou que nome é igual a Michel;
"Michel" : Informação armazenada temporariamente;

 As variáveis servem para guardar nomes, idades, resultados de cálculos e textos digitados pelo usuário.
 Um exemplo prático de como as variáveis são importantes.
 Imagina que queremos imprimir o nome de alguém várias vezes. 
 
 Sem variáveis:
 print("Michel")
 print("Michel")
 print("Michel")
 
 Agora imagina que queremos trocar o nome para "João"... Teríamos que mudar em todas as linhas.
 
 Com Variáveis:
 nome = "Michel"
 print(nome) #o resultado seria print("Michel")
 print(nome)
 print(nome)
 
 Agora imagina que queremos trocar o nome para "João"... Teríamos apenas que mudar o nome da variável de nome = "Michel"
 para nome = "João" e automaticamente mudaria rapidamente todas as informações, isso vale também para idade e outros conteúdos guardados.
 
 Atenção: usamos aspas duplas (" ") em um programa, quando queremos guardar um valor (conteúdo/informação), precisamos coloca-ló dentro de aspas duplas (" ").
 Isso é importante porque o computador entende que estamos a lidar com valores (conteúdo/informação) do tipo textual. Já os números como
 24 ou 1.85, não precisam de aspas.
 Outro ponto importante, a variável precisa ser única para cada tipo de valor armazenado. As variáveis funcionam como caixas que guardam 
 informações, então, se dermos o mesmo nome a duas variáveis diferente, o valor da primeira será perdido e substituído pelo novo.
 
 Nomeclatura das Variáveis: As Variáveis em Python podem conter apenas Letras, maiúsculas e minúsculas, número(com exceção na primeira posição
 no nome da variável) e underline (_). Além disso, não podemos utilizar algumas palavras que são restritas do Python como:
 if, input, while, for e etc...
 '''

#Exemplos
nome = "Etelvino Joaquim"
meucachoro = "Winnie" 
idade = 24
morada = "Bairro Camama, Rua Nº 11"
curso = "Contabilidade"
altura = 1.85
print("Nome Completo:", nome)
print("Nome do Cão:", meucachoro)
print("Idade:", idade)
print("Residência:", morada)
print("Altura:", altura)

#Podemos também criar variáveis numa única linha.
pele, olhos, cabelo, namorada, filhos = "Clara", "Castanhos descarregado", "Curto e preto", "Não", 0 

#Agora para imprimir utilizaremos esse método
print(f"Cor da pele: {pele} | Cor dos Olhos: {olhos} | Cabelo: {cabelo} | Casado: {namorada} | Filhos: {filhos}")

#Ao observar na impressão, veremos que as informações são expressas em linhas.
#Para imprimir em vertical usaremos apenas \n e apagaremos as |
print(f"Cor da pele: {pele} \nCor dos Olhos: {olhos} \nCabelo: {cabelo} \nCasado: {namorada} \nFilhos: {filhos}")

#Lembrando quando falamos que a variável precisa ser única para cada tipo de valor armazenado. 
#Se dermos o mesmo nome a duas variáveis diferente, o valor da primeira será perdido e substituído pelo novo
print("\n")
x = 1
y = 2
x = y
print("X:", x)
print("Y:", y)

#OPERADORES
'''
Operações básicas em Python são comandos que permitem realizar cálculos matemáticos simples, como SOMAR, SUBTRAIR, MULTIPLICAR e DIVIDIR.
Elas funcionam como ferramentas fundamentais para resolver problemais numéricos, criar lógicas de programação e desenvolver algoritmos.
'''
#Principais Operações Aritméticas em Python:
'''
Operações       |   Símbolos   |   Exemplo em Python   |   Ressultado
Adição          |      +       |        3 + 2          |      = 5
Subtração       |      -       |        5 - 2          |      = 3
Multiplicação   |      *       |        5 * 3          |      = 15
Divisão         |      /       |       15 / 2          |      = 7.5
Divisão Inteira |     //       |       6 // 3          |      = 2
Resto (Módulo)  |     %        |        9 % 2          |      = 1
Potenciação     |     **       |       2 ** 3          |      = 8
'''

'''
Divisão: divisão com / retorna um número com casas decimais (float), mesmo que a conta dê exta. A divisão é útil quando
queremos ver o valor completo, inclusive com os centavos ou as partes quebradas do número.

Divisão Inteira: divisão com dupla // retorna só a parte inteira da divisão, descartando tudo que vier depois da vírgula
(sem arredondar). A divisão inteira é útil quando queremos saber quantas vezes algo "cabe inteiro" dentro de outro.
Exemplo: "Quantas pizzas inteira posso comprar com 20 kz se cada uma custa 6 kz?" 20 // 6 = 3 (sobra 2, mas só podemos
comprar 3 inteiras).

Resto (Módulo): Quando dividimos dois números, o módulo é  o que sobra dessa divisão, em python usamos o símbolo %.
Operador % retorna o que sobra da divisão inteira entre dois números. 
Por exemplo, imagina que queremos saber quantas vezes o 6 cabe dentro do 20 sem passar?
6 x 3 = 18 - cabe 3 vezes inteiras.
Quanto sobra de 20 depois de tirar 18?
20 - 18 = 2
Então: 20 % 6 = 2

O resto é útil quando você quer verificar se um número é par ou ímpar. Saber se um número é divisível por outro
se a % b == 0, então a é divisível por b.
'''
print("\n")
print("Adição +")
#Operador de Adição +
a, b, c = 10, 12, 2
soma = a + b + c
soma2 = a + c
soma3 = a + b
soma4 = c + b
print(f"Resultado: {soma} \nResultado: {soma2} \nResultado: {soma3} \nResultado: {soma4}")

print("\n") #utilizei esse código para dar espaçamento entre as linhas
#Operador de Subtração
print("Subtração -")
sub = soma - a
sub1 = b - a
sub2 = soma3 -soma2
sub3 = a - c
sub4 = soma4 - b
print(f"Resultado: {sub} \nResultado: {sub1} \nResultado: {sub2} \nResultado: {sub3} \nResultado: {sub4}")

print("\n")
#Operador de Multiplicação
print("Multiplicação *")
mult = a * c
mult2 = mult * c
mult3 = sub3 * soma2
mult4 = b * c
print(f"Resultado: {mult} \nResultado: {mult2} \nResultado: {mult3} \nResultado: {mult4}")

print("\n")
#Operador de Divisão
print("Divisão / & //")
div = mult2 / c
div2 = div // sub2
div3 = mult3 / sub3
div4 = mult4 // sub3
div5 = 25 / 5
div6 = 15 / 2
print(f"Resultado: {div} \nResultado: {div2} \nResultado: {div3} \nResultado: {div4} \nResultado: {div5} \nResultado: {div6}")

print("\n")
#Operador de Resto (Módulo)
print("Resto %")
rest = mult2 % mult
rest2 = mult % c
rest3 = mult % div4
rest4 = a % div4
rest5 = 20 % 6
print(f"Resultado: {rest} \nResultado: {rest2} \nResultado: {rest3} \nResultado: {rest4} \nResultado: {rest5}")

print("\n")
#OPeradores de Potencia
print("Potência **")
pot = a ** c
pot2 = 3 ** 3
pot3 = 30 ** 2
print(f"Resultado: {pot} \nResultado: {pot2} \nResultado: {pot3}")

print("\n")
#Mais Algumas Operações Importantes
'''
Além das operações básicas, no Python (e em outras linguagens), possuímos algumas operações juntas com atribuições como 
+=, -= e *= .
Suponhamos que declaramos novamente duas variáveis:
 X = 6
 Y = 3
 Se caso quiséssemos fazer uma adição da variável X com o número inteiro 4, poderíamos fazer:
 X = X + 4 , correto ?
 Por baixo dos panos temos:
 6 = 6 + 4,  neste caso como o sinal de “=” é ATRIBUIÇÃO o valor da variável X mudará para 10.
 
Mas ao invés de fazermos desta forma mais longa (X = X + 4), podemos utilizar a seguinte Operação X += 4.
'''
#Exemplo
x = 8
y = 4
x = y + 2 #Por baixo dois panos temos: 8 = 4 + 2
print("Resultado:", x)

print("\n")
#Outra forma
z = 4
w =  5
z *= 3
n = z + x
print("Resultado:", x)
print("Resultado:", n)

print("Resultado:", x)









