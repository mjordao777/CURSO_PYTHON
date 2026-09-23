# ==============================================================================
# DESAFIO 1: Trabalho Simultâneo em Equipe (Comandos GIT Remoto)
# ==============================================================================
# CONCEITO: O "Git" é um sistema que os programadores usam para trabalhar em 
# equipe. Pense nele como uma "pasta compartilhada na internet" (como o Google 
# Drive), mas super inteligente, que guarda o histórico de tudo que foi feito.
# A função 'print()' serve para o computador "falar" com a gente, mostrando um
# texto na tela.

print("A) git clone: copia um repositório remoto para a máquina local.")
# EXPLICAÇÃO: "Clone" (clonar) é como baixar uma cópia idêntica de um projeto da
# internet para o seu computador pessoal, para você poder trabalhar nele offline.

print("B) git push: envia as alterações do repositório local para o repositório remoto.")
# EXPLICAÇÃO: "Push" (empurrar) é pegar o trabalho que você terminou no seu 
# computador e enviar para a internet, para que seus colegas possam ver e usar.

print("C) git pull: baixa e integra as alterações do repositório remoto para o repositório local.")
# EXPLICAÇÃO: "Pull" (puxar) é o contrário do push. É você pedir para o sistema: 
# "Baixe para o meu computador tudo o que os meus colegas fizeram de novo".

# ==============================================================================
# DESAFIO 2: Simulação de Desastres (Recuperação de Arquivos)
# ==============================================================================
# CONCEITO: O que acontece se o seu computador quebrar e você perder tudo? 
# Como o Git guarda tudo na internet (o que chamamos de "remoto"), você está seguro.

print("git clone: recupera o projeto completo do repositório remoto.")
# EXPLICAÇÃO: Se você comprou um computador novo, você usa o "clone" para baixar 
# tudo de volta e começar a trabalhar como se nada tivesse acontecido.

print("git pull: atualiza o projeto local com os arquivos do repositório remoto.")
# EXPLICAÇÃO: Se você só perdeu o trabalho de hoje, o "pull" puxa as últimas 
# versões salvas pela sua equipe para você não ter que recomeçar do zero.

# ==============================================================================
# DESAFIO 3: Controle de Acesso ao Servidor (Condicional if / else)
# ==============================================================================
# CONCEITO: Aqui ensinamos o computador a tomar decisões.
# Primeiro, criamos uma "variável". Imagine uma variável como uma caixa com uma 
# etiqueta. A caixa se chama 'senha_digitada', e dentro dela guardamos o 
# texto "DevSec2026".

senha_digitada = "DevSec2026"

# O comando 'if' significa "SE" em inglês. É o computador fazendo uma pergunta.
# A pergunta é: O texto dentro da caixa 'senha_digitada' é EXATAMENTE IGUAL (==)
# à senha correta, que é "JWC@Admin"?
if senha_digitada == "JWC@Admin":
    # Se a resposta for SIM (verdadeiro), o computador executa a linha abaixo:
    print("Acesso Liberado.")
    
# O comando 'else' significa "SENÃO". 
else:
    # Se a resposta for NÃO (a senha é diferente), ele ignora a linha de cima 
    # e executa a linha abaixo, barrando o usuário:
    print("Acesso Negado!")

# ==============================================================================
# DESAFIO 4: Classificação de Ameaças (Condicionais if / elif / else)
# ==============================================================================
# CONCEITO: E se precisarmos tomar uma decisão com mais de duas opções? 
# Usamos o 'elif', que significa "SE NÃO FOR O ANTERIOR, MAS FOR ESTE...".

# Colocamos o número 3 dentro da caixa (variável) chamada 'nivel_ameaca'.
nivel_ameaca = 3

# Pergunta 1: O nível de ameaça é 1? (Falso, é 3)
if nivel_ameaca == 1:
    print("Baixa: Adicionar ao Backlog da Sprint.")
    
# Pergunta 2: Já que não é 1, o nível de ameaça é 2? (Falso, é 3)
elif nivel_ameaca == 2:
    print("Média: Desenvolvedor deve revisar hoje.")
    
# Pergunta 3: Já que não é 1 nem 2, o nível é 3? (Verdadeiro!)
elif nivel_ameaca == 3:
    # Como isso é verdade, o computador executa esta linha e pula o resto.
    print("Alta/Crítica: Acionar Matheus (DevSecOps) imediatamente!")
    
# O 'else' final é o "cesto de lixo". Se NENHUMA das perguntas acima for verdade, 
# ele cai aqui por padrão.
else:
    print("Nível não reconhecido.")

# ==============================================================================
# DESAFIO 5: Menu de Ferramentas (Switch Case)
# ==============================================================================
# CONCEITO: O 'match / case' é uma forma mais elegante de fazer várias perguntas.
# Imagine um menu de restaurante onde cada número é um prato diferente. Em vez de
# perguntar "É o prato 1? É o prato 2?", o computador vai direto para o número escolhido.

# Guardamos o número 2 na caixa 'opcao_menu'.
opcao_menu = 2

# O comando 'match' diz: "Olhe para o que está dentro da caixa opcao_menu".
match opcao_menu:
    # Caso (case) o número lá dentro seja 1:
    case 1:
        print("Iniciando varredura SAST no código fonte...")
        
    # Caso (case) o número seja 2 (Este é o nosso caso! Ele vai executar a linha abaixo):
    case 2:
        print("Iniciando processo de sanitização de metadados...")
        
    # Caso (case) o número seja 3:
    case 3:
        print("Gerando relatório OWASP de vulnerabilidades...")
        
    # O 'case _' funciona igual ao 'else' do exemplo anterior. Se o usuário 
    # digitar um número que não existe no menu (como 4 ou 99), ele dá uma mensagem de erro.
    case _:
        print("Opção inválida. Tente novamente.")