
# O que são?
'''
Os operadores and e or são usados para combinar condições.
and: Todas as condições são verdadeiras;
or: Basta uma condição ser verdadeira.
'''

# Por que usamos?
'''
Usamos and e or quando queremos avaliar mais de uma condição ao mesmo tempo, como em:
Formulário de acesso (login e senha corretos);
Decisões baseadas em idade E nacionalidade;
Situações em que uma coisa OU outra já é suficiente
'''

# OPERADOR com and
'''
Imagine que você queira validar se 2 variáveis obedecem uma condição, caso contrário você ignora e sair do programa.
Para isso podemos utilizar o operador and(E). Se caso TODAS as sentenças forem VERDADEIRAS em sua CONDIÇÃO, o
processo é marcado como TRUE.
'''
# Exemplo
variavel = 1
variavel1 = 2

if variavel == 1 and variavel1 == 2:
    print(True)
else:
    print(False)

# Porém se uma das validações forem falsas o processo é tido como FALSE.
if variavel == 1 or variavel1 == 3:
    print(True)
else:
    print(False)

print("\n")
# A pessoa só pode entrar se for maior de 18 e tiver documento.
idade = 20
documento = True
if idade >= 18 and documento == True:
    print("Pode entrar")
else:
    print("Não pode entrar")

# A pessoa só pode entrar se tiver dinheiro ou convite
tem_dinheiro = False
tem_convite = True

if tem_dinheiro and tem_convite:
    print("Pode entrar")
else:
    print("Não pode entrar")

'''
Operador
and: Quando todas as condições forem verdadeira;
or: Quando pelo menos uma é verdadeira;
'''
tem_chave = False
tem_controle = True
if tem_chave and tem_controle:
     print("pode entrar")
else:
     print("A porta trancou")