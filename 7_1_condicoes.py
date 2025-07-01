# 🧠 CONDIÇÕES EM PYTHON
'''
Em toda linguagem de programação precisamos de condições para tomarmos uma decisão.
Condições nada mais são, do que sentenças para descobrir se a lógica é VERDADEIRA ou FALSA.

Imagina que você está a criar o sistema de compras de uma loja online. Os clientes fazem compras e, dependendo do valor total,
podem ganhar fretes grátis.

A regra da loja é simples:
Se o valor total da compra for igual ou superior a 10.000 kz, o frete será gratuito.
Se for menos, o frete custará 1.000 kz.

Como as condições entram nesse cenário?
  Você precisa de um mecanismo inteligente dentro do programa que:
  Verifique o valor total da compra do cliente;
  Compare esse valor com o limite de 10.000 kz;
  E escolher o que fazer:
    Se a condição for satisfeita (compra >= 10.000 kz ): aplicar fretes grátis.
    Se a condição não for satisfeita (compra < 10.000 kz): adicionar fretes de 1.000 kz.

Por que é importante?
 Sem condições, o sistema trataria todas as compras do mesmo jeito, o que quebraria a lógica da programação.
 Com as condções, o programa decide o que fazer co base em regras, tornando-se inteligente, útil e justo.

Moral:
 As condições tornam o programa capaz de tomar decisões, igual a um ser humano.
 Elas são o coração da lógica de qualquer aplicação interativa
'''



'''
numeroUm == 1
numeroDois == 2
Símbolo | Descrição        | Exemplos
==      | IGUAL            | numero1 == numero2
        |                  | False
        |                  |
!=     | DIFERENTE         | numeroUm != numeroDois
        |                  | True
        |                  |
<       | MENOR            | numeroUm < numeroDois
        |                  | True  
        |                  |          
<=      | MENOR OU IGUAL   | numeroTres <= numeroQuatro
        |                  | True
        |                  |
>       | MAIOR            | numeroUm > numeroDois
        |                  | False
        |                  |
>=      | MAIOR OU IGUAL   | numeroTres >= numeroQuatro
        |                  |True
'''

# == (Igual) Verifica se os dois elementos são iguais ou não, se for igual retorna VERDADEIRO se não volta FALSO;
# != (Diferente) Verifica se os dois elementos são diferentes ou não, se for diferente retorna VERDADEIRO se não volta FALSO;
# < (Menor) Caso o primeiro elemento seja menor que o segundo retorna VERDADEIRO, caso contrário retorna FALSO;
# <= (Menor Igual) Caso o primeiro elemento seja MENOR ou IGUAL ao segundo elemento retorna Verdadeiro, se não volta FALSO;
# > (Maior) Caso o primeiro elemento seja MAIOR que o segundo retorna VERDADEIRO, se não retorna FALSO;
# >= (Maior igual) Caso o primeiro elemento seja MAIOR ou IGUAL ao segundo retorno VERDADEIRO, se não retorna FALSO.

# Por que usamos condições?
# Validar dados
# Fazer perguntas ao usuário e responder de acordo
# Controlar o fluxo do programa
# Criar Interatividade

# Estrutura básica
# if condição:
    # Código se a condição for verdadeira

# Mas também podemos usar:
    # if condição:
         # código se for verdadeiro
    # elif outra condição:
         # código se a primeira não for verdadeira, mas essa sim
    # else:
       # código se nenhuma das anteriores for verdadeira

print("\n")

# Exemplo simples com if
idade = 20
if idade > 18:
    print("Você é maior de idade.")

# Exemplo com if...else
idade = 16
if idade > 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade")

# Exemplo com if...elif...else
nota = 65
if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Bom")
else:
    print("Reprovado")

# Conclusão
# Use if para a primeira verificação.
# Use elif para quantas condições intermediárias forem necessárias.
# Use else opcionalmente para o caso final, quando nenhuma das condições anteriores for verdadeira.

# O papel de if, elif e else
'''
if
Aqui testamos uma condição. Se for verdadeira, o bloco de código é executado.
      if idade >= 18
         print("Maior de idade")

elif
É uma nova condição que só é verificada se o if anterior for falso.
      elif idade >= 13
        print("Adolescente")
        
Podemos ter quantos elif forem necessários, dependendo das possibilidades que queremos testar.


else
Não recebe condição.
O else entra automaticamente quando nenhuma das condições anteriores (if e elif) for satisfeita.
É como um "plano B" automático, um caminho final padrão para quando tudo o que foi testado antes de falhar.

      else
        print("Criança")        
'''

# Por que o else não recebe condição?
'''
Porque ele não precisa testar nada. Ele só existe para lidar com todos os casos que não se enquadram nas condições anteriores.
Isso torna o código mais limpo, evita repetir condições, e serve como uma garantia de respostas final.
'''

print("\n")

# Exemplo completo
idade1 = 10
if idade1 >= 18:
    print("Adulta")
elif idade1 >= 13:
    print("Adolescente")
else:
    print("Criança")

# Nesse caso:
# Se idade for 18 ou mais, "imprime adulta";
# Se idade for 13 ou mais, imprime "Adolescente";
# Se nenhuma dessas for verdadeira (como é o caso com idade 10), o else assume automaticamente e imprime "Criança"