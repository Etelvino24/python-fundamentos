# O comando break é usado dentro de laços de repetição (for ou while) e serve para interromper a repetição antes do fim,
# quando uma certa **condição for atendida.

# ✅ O que o break faz?
# Ele quebra (interrompe) o laço no momento em que é executado, mesmo que ainda existam repetições a serem feitas.

# 🧠 Por que usar?
# Usamos o break quando:

# 📌 Já **encontramos o que procurávamos** e não precisamos continuar.
# 📌 Há uma **condição de parada antecipada.
# 📌 Queremos melhorar a performace, evitando repetições desnecessárias.


### 📌 Exemplo 1: Parar quando encontrar um número específico
for numero in range(1, 10):
    print(numero)
    if numero == 5:
        print("Número 5 encontrado. Parando o loop.")
        break

# 🔎 Saída:
''''
1
2
3
4
5
Número 5 encontrado. Parando o loop.
'''

### 📌 Exemplo 2: Procurando um nome
nomes = ["Ana", "João", "Etelvino", "Carlos"]

for nome in nomes:
    if nome == "Etelvino":
        print("Nome encontrado!")
        break
    print(f"Verificando {nome}...")


### ⚠️ Dica importante
# Se o break for executado, nenhum código após ele dentro do laço será executado na repetição atual.

# 👀 Resumindo:
'''
| Palavra-chave | Função                          |
| ------------- | ------------------------------- |
| `break`       | Interrompe o laço imediatamente |
'''


# 🔄 Como o break funciona no while?


## 🔧 Estrutura básica:
'''
while condição:
    # instruções
    if outra_condição:
        break
    # mais instruções
'''

# 🧪 Exemplo didático:
# 💬 Situação:

# Vamos fazer um programa que pede uma senha, e só continua se estiver correta. Se o usuário digitar "sair",
# ele para imediatamente.

while True:  # laço infinito
    senha = input("Digite sua senha: ")

    if senha == "1234":
        print("Senha correta! Bem-vindo.")
        break  # Sai do laço se a senha for correta

    if senha == "sair":
        print("Encerrando o programa.")
        break  # Também sai se o usuário digitar 'sair'

    print("Senha incorreta. Tente novamente.")

# 🧭 Etapas do exemplo:
'''
1. O while True: cria um laço infinito, ou seja, que nunca para sozinho.
2. O break é usado em **dois casos**:

   * Quando a senha for "1234"
   * Quando a pessoa quiser encerrar com "sair"
3. Em qualquer um desses casos, o break força o Python a sair do laço.
'''

# 🎯 Por que usar o break?

# 📌 Segurança: evita laços infinitos desnecessários.
# 📌 Controle: permite sair do laço quando uma condição específica** acontecer.
# 📌 Clareza: o código fica mais simples de entender, pois você define com clareza o ponto de saída.


# O comando continue em Python serve para pular a iteração atual do laço (for ou while) e ir diretamente para a próxima
# repetição, ignorando o que vem depois dele **dentro do laço naquela rodada**.

# 🧠 Por que usamos o continue?

# Usamos o continue quando:

# 📌 Não queremos executar parte do código se uma certa condição acontecer.
# 📌 Queremos "ignorar" certos dados ou situações específicas durante a repetição.

# ✅ Exemplo com for
for numero in range(1, 6):
    if numero == 3:
        continue  # pula a impressão do número 3
    print(f"Número: {numero}")

print("\n")

# ✅ Exemplo com while
contador = 0
while contador < 5:
    contador += 1
    if contador == 3:
        continue  # pula a impressão do número 3
    print(f"Contador: {contador}")

### ⚠️ Importante:

# No while, cuidado com o continue: se você colocá-lo antes de atualizar a variável de controle, pode causar um loop
# infinito!

# 🧩 Quando usar o continue?
# 📌 Quando você está lendo uma lista de dados e quer **pular** itens vazios ou inválidos.
# 📌 Quando você quer **manter o laço**, mas ignorar **alguns valores específicos**.
# 📌 Em **validações dentro de laços**, para seguir direto para o próximo item.


# 🤔 O que é a **variável de controle** no while?

# É a variável que decide quando o laço termina. No exemplo abaixo, contador é essa variável:
'''
contador = 0
while contador < 5:
    print(contador)
    contador += 1  # <- isso é a atualização da variável de controle
'''


# ⚠️ Agora veja o que acontece com o `continue` mal colocado:

'''
contador = 0
while contador < 5:
    if contador == 3:
        continue
    print(contador)
    contador += 1
'''

# 🛑 Isso vai gerar um loop infinito quando contador == 3.

# 🎯 Por quê?
# Porque quando contador == 3, o programa entra no if, executa continue e pula diretamente para o próximo ciclo, sem
# aumentar o contador (contador += 1).
# Resultado? O `contador` **nunca sai do 3, e o laço **repete para sempre.


# ✅ Solução correta:
'''
contador = 0
while contador < 5:
    if contador == 3:
        contador += 1  # atualiza ANTES de pular
        continue
    print(contador)
    contador += 1
'''

# 📌 Agora sim: quando chegar no 3, ele aumenta o contador antes de continuar, evitando o laço infinito.

# 🧠 Resumo:
# 📌 No while, sempre atualize a variável de controle ANTES do continue.
# 📌 Se não fizer isso, o valor nunca muda e o laço nunca termina.
