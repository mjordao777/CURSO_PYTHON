
# ==============================================================================
# CADERNO DE DESAFIOS - AULA 2: O PRIMEIRO DIA NA JWC
# ==============================================================================
# CONCEITO GERAL: Nesta aula, vamos aprender os fundamentos da comunicação com o 
# computador. Vamos ensiná-lo a falar (print), a escutar (input) e a guardar 
# informações na memória usando caixinhas chamadas "variáveis".

# ==============================================================================
# DESAFIO 1: A Chegada ao Centro
# ==============================================================================
# CONCEITO: A função 'print()' é a "boca" do computador. É como mandamos ele 
# escrever algo na tela. Tudo que for TEXTO deve estar sempre entre aspas ("").

print("Cheguei na JWC!")
# EXPLICAÇÃO: O computador vai ler isso e mostrar exatamente a frase na tela.

# ==============================================================================
# DESAFIO 2: O Crachá de Visitante
# ==============================================================================
# CONCEITO: Uma "variável" é como uma caixa organizadora com uma etiqueta.
# Nós damos um nome a ela (a etiqueta) e guardamos uma informação lá dentro.

# Criamos a caixa 'nome_candidato' e guardamos o texto "Caio Barbosa".
nome_candidato = "Caio Barbosa"

# Criamos a caixa 'idade_candidato' e guardamos o número 50 (números não usam aspas!).
idade_candidato = 50

# Agora pedimos para o computador mostrar o que tem DENTRO das caixas.
print(nome_candidato)
print(idade_candidato)

# ==============================================================================
# DESAFIO 3: Conhecendo a Estrutura
# ==============================================================================
# CONCEITO: O computador é ótimo com matemática. Podemos fazer contas usando as 
# nossas caixas (variáveis) em vez de usar os números diretamente.

total_colaboradores_administrativos = 30
total_colaboradores_desenvolvimento = 20

# Aqui criamos uma terceira caixa que vai guardar o resultado da SOMA (+) das outras duas.
total_geral_funcionarios = total_colaboradores_administrativos + total_colaboradores_desenvolvimento

print(total_geral_funcionarios)

# ==============================================================================
# DESAFIO 4: O Boom da Educação
# ==============================================================================
# CONCEITO: Quando queremos criar uma caixa cujo valor NUNCA deve ser alterado, 
# nós a chamamos de "Constante". Por convenção (um acordo entre programadores),
# escrevemos o nome dela todo em MAIÚSCULAS para avisar: "Não mexa aqui!".

SETOR_MERCADO_PRINCIPAL = "Educação"

# O sinal de mais (+) quando usado com textos serve para "colar" (concatenar) um no outro.
print("Um dos setores que recebe mais investimento é o da " + SETOR_MERCADO_PRINCIPAL)

# ==============================================================================
# DESAFIO 5: O Armário do RH
# ==============================================================================
# CONCEITO: Fixando a diferença visual. MAIÚSCULAS para coisas fixas (Constantes),
# minúsculas para coisas que podem mudar ao longo do tempo (Variáveis).

NOME_EMPRESA = "JWC" # Constante: O nome da empresa não muda.
status_atual_candidato = "Em teste" # Variável: O status do candidato vai mudar depois.

print(NOME_EMPRESA)
print(status_atual_candidato)

# ==============================================================================
# DESAFIO 6: Conversa no Cafezinho
# ==============================================================================
# CONCEITO: A função 'input()' é o "ouvido" do computador. Ela faz o programa pausar,
# faz uma pergunta na tela e espera o usuário digitar uma resposta no teclado.

# A resposta que o usuário digitar será guardada na caixa 'linguagem_favorita'.
linguagem_favorita = input("Qual é a sua linguagem favorita? ")

# Depois, o computador mostra o que ele acabou de escutar e guardar.
print(linguagem_favorita)

# ==============================================================================
# DESAFIO 7: O Formulário de Transporte
# ==============================================================================
# CONCEITO: Praticando a coleta de dados (input). Todo sistema precisa receber 
# dados de alguém (do teclado, do mouse, da tela do celular).

meio_transporte_utilizado = input("Qual seu meio de transporte?: ")
print(meio_transporte_utilizado)

# ==============================================================================
# DESAFIO 8: Mudança de Planos
# ==============================================================================
# CONCEITO: Por que se chama "Variável"? Porque o valor pode VARIAR! 
# Se você colocar algo novo em uma caixa que já estava cheia, o conteúdo antigo 
# é jogado fora e substituído pelo novo.

# A caixa recebe o valor "Estágio".
cargo_pretendido_candidato = "Estágio"
print(cargo_pretendido_candidato)

# A MESMA caixa agora recebe o valor "Full Stack". O "Estágio" sumiu para sempre.
cargo_pretendido_candidato = "Full Stack"
print(cargo_pretendido_candidato)

# ==============================================================================
# DESAFIO 9: Avaliação de Perfil
# ==============================================================================
# CONCEITO: "Booleanos" (True ou False) são como interruptores de luz: Ligado ou Desligado,
# Sim ou Não, Verdadeiro ou Falso. 
# Importante: Em Python, eles PRECISAM começar com letra maiúscula (True / False) e não usam aspas.

possui_perfil_curioso = True
possui_perfil_agil = True
possui_perfil_inovador = True

print(possui_perfil_curioso)
print(possui_perfil_agil)
print(possui_perfil_inovador)

# ==============================================================================
# DESAFIO 10: O Grito do Diretor
# ==============================================================================
# CONCEITO: Textos em Python possuem "ferramentas" embutidas chamadas de "métodos".
# O método '.upper()' (do inglês "upper case" = letra maiúscula) pega qualquer 
# texto minúsculo e transforma em maiúsculo na hora de exibir.

mensagem_aviso_mural = "bem-vindos novos talentos"
print(mensagem_aviso_mural.upper())

# ==============================================================================
# DESAFIO 11: A Senha de Acesso
# ==============================================================================
# CONCEITO: A função 'len()' vem da palavra "length" (comprimento/tamanho em inglês).
# Ela serve para o computador contar quantos caracteres (letras, números, espaços) 
# existem dentro de um texto.

senha_temporaria_rede = "senha123"

# A senha tem a palavra "senha" (5 letras) + "123" (3 números) = 8 caracteres.
print(len(senha_temporaria_rede))

# ==============================================================================
# DESAFIO 12: Juntando os Pedaços
# ==============================================================================
# CONCEITO: Ao "colar" (concatenar) variáveis de texto usando o sinal de mais (+), 
# o computador junta tudo exatamente do jeito que está. Se você não colocar um 
# espaço manualmente (" "), as palavras ficarão grudadas ("ArthurSilva").

primeiro_nome = "Arthur"
sobrenome_candidato = "Silva"

# Juntando: "Arthur" + " " (espaço vazio) + "Silva" = "Arthur Silva"
nome_completo_formatado = primeiro_nome + " " + sobrenome_candidato

print(nome_completo_formatado)

# ==============================================================================
# DESAFIO 13: Cálculo do Benefício
# ==============================================================================
# CONCEITO: O sinal de mais (+) é inteligente. 
# - Se as variáveis forem TEXTOS (com aspas), ele junta as palavras.
# - Se as variáveis forem NÚMEROS (sem aspas), ele faz a conta de matemática (soma).

valor_salario_base = 2000
valor_auxilio_ferramentas = 150

# Aqui ele entende que é matemática, então 2000 + 150 vira 2150.
total_remuneracao_inicial = valor_salario_base + valor_auxilio_ferramentas

print(total_remuneracao_inicial)

# ==============================================================================
# DESAFIO 14: O Bug do Código
# ==============================================================================
# CONCEITO: O computador é burro e obedece regras estritas. Texto SEMPRE precisa 
# de aspas (duplas "" ou simples ''). Se você não colocar, o computador acha que as 
# palavras são comandos ou variáveis que não existem, causando um "Erro de Sintaxe".

# CORREÇÃO: O texto informativo precisa estar envolto em aspas.
texto_informativo = "Alerta do sistema interno da JWC"
print(texto_informativo)

# ==============================================================================
# DESAFIO 15: O Relatório de Fim de Dia (Projeto Final da Aula)
# ==============================================================================
# CONCEITO: Aqui juntamos tudo o que aprendemos e introduzimos a 'f-string'.
# Colocar um 'f' minúsculo antes das aspas de um print (f"...") permite "injetar" 
# as nossas caixinhas (variáveis) diretamente no meio do texto, apenas colocando-as 
# entre chaves { }. É muito mais fácil do que usar o símbolo de mais (+).

nome_colaborador_input = input("Qual o nome do Colaborador? ")
idade_colaborador_input = input("Qual é a idade do Colaborador? ")
pontuacao_teste_pratico = input("Qual é a pontuação do teste prático? ")

# EXPLICAÇÃO: Em vez de fazer print("Nome: " + nome + ", Idade: " + idade...), 
# usamos a formatação 'f-string' para deixar o código limpo e elegante!
print(f"Nome: {nome_colaborador_input}, Idade: {idade_colaborador_input}, Pontuação: {pontuacao_teste_pratico}")