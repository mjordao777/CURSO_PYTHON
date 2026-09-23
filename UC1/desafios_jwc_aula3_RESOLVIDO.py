# ==============================================================================
# CADERNO DE DESAFIOS - AULA 3: GIT E EXPRESSÕES ARITMÉTICAS
# Empresa: JWC Tecnologia
# Módulo: Programador Full Stack - Processo Seletivo
# ==============================================================================
# CONCEITO GERAL: Nesta aula, o foco é entender a diferença entre Git e GitHub,
# aprender os comandos básicos de versionamento no próprio computador e, por fim, 
# usar o Python como uma calculadora poderosa para resolver problemas do dia a dia.

# ==============================================================================
# DESAFIO 1: O Onboarding com a Tech Lead (O Mundo do GIT)
# ==============================================================================
# CONCEITO: Existe uma grande confusão entre "Git" e "GitHub". 
# - O Git é o "programa" que você instala no seu computador. Ele gerencia as 
#   versões do seu projeto (como uma máquina do tempo dos seus arquivos).
# - O GitHub é o "site" (a nuvem) onde você publica e compartilha esses arquivos
#   para trabalhar em equipe (como se fosse uma rede social para programadores).

print("A) O Git foi criado por Linus Torvalds. O GitHub foi criado por Tom Preston-Werner, Chris Wanstrath e P. J. Hyett, com Scott Chacon também entre os primeiros integrantes.")
print("B) O GitHub foi vendido para a Microsoft em 2018 por aproximadamente US$ 7,5 bilhões.")
print("C) Dois concorrentes do GitHub são GitLab e Bitbucket.")
# EXPLICAÇÃO: GitLab e Bitbucket são como "canais de TV diferentes". Eles fazem
# o mesmo serviço que o GitHub (guardar código na internet), mas são de outras empresas.

# ==============================================================================
# DESAFIO 2: O Padrão da Empresa (Comandos GIT)
# ==============================================================================
# CONCEITO: Como a gente salva o nosso trabalho usando o Git no nosso computador?
# Imagine que você está empacotando coisas para uma mudança.

print("1. Iniciar um novo repositório local: git init")
# EXPLICAÇÃO: 'init' (iniciar). É como pegar uma caixa de papelão vazia e dizer: 
# "Vou começar a guardar meu projeto aqui dentro".

print("2. Verificar o estado atual dos arquivos: git status")
# EXPLICAÇÃO: 'status'. É olhar para a caixa e ver o que está dentro, o que foi 
# modificado e o que ainda está fora da caixa.

print("3. Adicionar arquivos à área de preparação: git add .")
# EXPLICAÇÃO: 'add .' (o ponto significa 'tudo'). É você pegar todos os arquivos 
# novos ou modificados e colocá-los dentro da caixa.

print("4. Salvar as alterações com uma mensagem: git commit -m 'mensagem'")
# EXPLICAÇÃO: 'commit'. É você passar a fita adesiva na caixa, fechar e colar uma 
# etiqueta (a mensagem) dizendo: "Aqui dentro estão as alterações do dia 21".

# ==============================================================================
# DESAFIO 3: A Primeira Feature (Operador de Subtração -)
# ==============================================================================
# CONCEITO: O Python funciona como uma calculadora. Aqui usamos o símbolo de 
# menos (-) para fazer contas de subtração.

capacidade_total_escola = 850
alunos_matriculados = 523

# O computador pega o número 850, subtrai 523, e guarda o resultado (327) 
# dentro de uma nova caixa (variável) chamada 'vagas_disponiveis'.
vagas_disponiveis = capacidade_total_escola - alunos_matriculados

print("Vagas disponíveis:", vagas_disponiveis)

# ==============================================================================
# DESAFIO 4: Calculando o Faturamento (Operador de Multiplicação *)
# ==============================================================================
# CONCEITO: No mundo da programação, não usamos o "x" para multiplicar, 
# usamos o asterisco (*).

mensalidade_padrao = 850.50 # Números quebrados (decimais) usam ponto, não vírgula!
novas_matriculas = 42

faturamento_projetado = mensalidade_padrao * novas_matriculas

print("Faturamento projetado:", faturamento_projetado)

# ==============================================================================
# DESAFIO 5: Divisão de Turmas (Operador de Divisão /)
# ==============================================================================
# CONCEITO: Para dividir, usamos a barra (/). 
# Um detalhe: a divisão normal (/) sempre entrega um número decimal (mesmo que 
# a divisão seja exata, como 10 / 2, o computador mostra 5.0).

total_alunos_turma = 45
tamanho_grupo_ideal = 5

grupos_formados = total_alunos_turma / tamanho_grupo_ideal

print("Grupos formados:", grupos_formados)

# ==============================================================================
# DESAFIO 6: Lógica de Paginação (Divisão Inteira // e Resto %)
# ==============================================================================
# CONCEITO: E se precisarmos dividir coisas que não podem ser cortadas ao meio?
# Não podemos ter "33.3 tablets" em uma sala. Precisamos de números inteiros!

total_tablets = 100
total_salas = 3

# O operador // (duas barras) faz a "Divisão Inteira". 
# Ele ignora os decimais. Ele responde: "Quantos grupos inteiros cabem?" (Neste caso, 33).
tablets_por_sala = total_tablets // total_salas

# O operador % (sinal de porcentagem) não significa porcentagem aqui! 
# Na programação, ele é o "Módulo" ou "Resto da divisão". 
# Ele responde: "Se eu dividir 100 por 3 e der 33 pra cada, quantos sobram?" (Sobra 1).
tablets_sobra = total_tablets % total_salas

print("Tablets inteiros por sala:", tablets_por_sala)
print("Tablets que ficarão na reserva da TI:", tablets_sobra)

# ==============================================================================
# DESAFIO 7: Escalabilidade de Servidor (Exponenciação **)
# ==============================================================================
# CONCEITO: Como fazemos contas de "elevado a" (potência)? Usamos dois asteriscos (**).
# E assim como na matemática da escola, o que está entre parênteses () é resolvido primeiro.

armazenamento_atual_tb = 3

# Aqui o computador resolve (2 ** 4) primeiro, ou seja, 2 elevado à 4ª potência (2*2*2*2 = 16).
# Depois, ele multiplica o resultado por 3 (16 * 3 = 48).
armazenamento_futuro_tb = armazenamento_atual_tb * (2 ** 4)

print("Armazenamento necessário daqui a 4 anos:", armazenamento_futuro_tb, "TB")

# ==============================================================================
# DESAFIO 8: O MVP do Boletim Digital (Projeto Final da Aula 3)
# ==============================================================================
# CONCEITO: Aqui juntamos tudo e deixamos o programa interativo!

# 'input()' faz o computador parar e esperar o usuário digitar alguma coisa.
# O que o usuário digitar será guardado na caixa 'nome_aluno'.
nome_aluno = input("Digite o nome do aluno: ")

# O comando 'float()' transforma o texto que o usuário digitou em um "Número Decimal".
# Se não fizermos isso, o computador acha que o número é só um texto e não consegue somar.
nota1 = float(input("Digite a nota do 1º trimestre: "))
nota2 = float(input("Digite a nota do 2º trimestre: "))
nota3 = float(input("Digite a nota do 3º trimestre: "))

# Primeiro ele soma as notas (porque estão entre parênteses) e depois divide por 3.
media = (nota1 + nota2 + nota3) / 3

# EXPLICAÇÃO FINAL: O 'f' antes das aspas (f"Sistema...") significa "Formatação".
# Ele permite que a gente coloque as caixinhas (variáveis) no meio do texto,
# apenas colocando elas entre chaves {}. 
# O código ':.2f' dentro da chave da média serve para arredondar o número, 
# dizendo para o computador mostrar apenas 2 (dois) números após o ponto (f).
print(f"Sistema JWC: O aluno {nome_aluno} fechou o ano com média {media:.2f}")