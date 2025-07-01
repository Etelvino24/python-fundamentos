#Conversores
'''
Conversores são funções que usamos para mudar o tipo de um dado. Por exemplo, transformar um número em texto, um texto em
número, ou um número inteiro em número decimal.

Para que servem?
Servem para quando você precisa usar um valor de outro tipo, por exemplo:
Juntar um número com uma string (precisa converter para string).
Fazer contas com um número que veio como texto (precisa converter para número).
Arredondar, truncar ou ajustar valores numéricos
'''

# Principais Conversores em Python
'''
Conversor  | Significado                          | Exemplo
int()      | Converter para inteiro               | int("10") - 10
float()    | Converter para número decimal        | float("10.5") - 10.5
str()      | Converter para string (texto)        | str(25) - "25"
bool()     |Converter para booleano (True/False)  | bool(1) - True 
'''

#Exemplos
# Convertendo texto em número inteiro
numero = int("45")
print(numero + 10) # 55

print("\n")

# Convertendo número em texto
idade = 30
mensagem = "Idade: " + str(idade)
print(mensagem) # idade: 30

print("\n")

#Convertendo número inteiro em decimal
preco = float(1000)
print(preco + 0.22) # 1000.22

print("\n")

# Convertendo número para booleano
print(bool(0)) # False
print(bool(10)) # True

# Cuidado
# int("dez") Erro! "dez" não é número
# float("10.5") Erro! Precisa ser "10.5"

# Por que é importante usar conversores
'''
Na programação, os dados nem sempre vêm no formato que precisamos. E para garantir que o programa funcione corretamente,
precisamos converter esses dados. É aí que entram os conversores.
'''
# 1- Tipos diferentes não se misturam
'''
Você não pode somar um número com um texto diretamente. Por exemplo:

idade = 25
mensagem = "Sua idade é " + idade
print(mensagem) # Isso da Erro!
Esse erro acontece porque o Python não sabe somar texto com número. Mas se você converter o número em texto com str(): 
'''
idade = 24
mensagem = "Olá, o meu nome é Etelvino Joaquim e eu tenho " + str(24) + " de idade." # Agora funciona
print(mensagem)

print("\n")

# 2- Dados externos vêm como texto (string)
'''
Quando oo usuário digita algo, ou quando você lê de um arquivo ou site, dados quase sempre chegam como texto.

entrada = input ("Digite sua idade: ")
print(entrada + 5)   # Isso da Erro!
'''
# Para resolver convertemos
entrada = 20
idade = int(entrada)
print(idade + 2)

# 3- Boas prática e segurança
'''
Conversores permitem que o programa verifique e controle os tipos de dados que está lidando. Isso evita bugs e torna o 
código mais seguro e confiável.
'''

# 4- Mais flexibilidade
'''
Conversores te ajudam a:
Formatar valores para exibir ao usuário (número - texto)
Fazer cálculos com entradas que nates eram texto
Validar condições com bool()
Trabalhar com dados que vêm da internet, banco de dados, arquivos, etc.
'''

# Conclusão
'''
Conversores são como tradutores: eles transformam os dados no idioma certo para que o Python possa entender e trabalhar
com eles corretamente.

Sem eles, o programa trava, erra ou simplesmente não faze o que deveria fazer.
'''

