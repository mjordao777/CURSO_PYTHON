
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

# EXPLICAÇÃO: O computador vai ler isso e mostrar exatamente a frase na tela.

# ==============================================================================
# DESAFIO 2: O Crachá de Visitante
# ==============================================================================
# CONCEITO: Uma "variável" é como uma caixa organizadora com uma etiqueta.
# Nós damos um nome a ela (a etiqueta) e guardamos uma informação lá dentro.

# Criamos a caixa 'nome_candidato' e guardamos o texto "Caio Barbosa".

# Criamos a caixa 'idade_candidato' e guardamos o número 50 (números não usam aspas!).

# Agora pedimos para o computador mostrar o que tem DENTRO das caixas.


# ==============================================================================
# DESAFIO 3: Conhecendo a Estrutura
# ==============================================================================
# CONCEITO: O computador é ótimo com matemática. Podemos fazer contas usando as 
# nossas caixas (variáveis) em vez de usar os números diretamente.



# Aqui criamos uma terceira caixa que vai guardar o resultado da SOMA (+) das outras duas.


# ==============================================================================
# DESAFIO 4: O Boom da Educação
# ==============================================================================
# CONCEITO: Quando queremos criar uma caixa cujo valor NUNCA deve ser alterado, 
# nós a chamamos de "Constante". Por convenção (um acordo entre programadores),
# escrevemos o nome dela todo em MAIÚSCULAS para avisar: "Não mexa aqui!".


# O sinal de mais (+) quando usado com textos serve para "colar" (concatenar) um no outro.

# ==============================================================================
# DESAFIO 5: O Armário do RH
# ==============================================================================
# CONCEITO: Fixando a diferença visual. MAIÚSCULAS para coisas fixas (Constantes),
# minúsculas para coisas que podem mudar ao longo do tempo (Variáveis).


# ==============================================================================
# DESAFIO 6: Conversa no Cafezinho
# ==============================================================================
# CONCEITO: A função 'input()' é o "ouvido" do computador. Ela faz o programa pausar,
# faz uma pergunta na tela e espera o usuário digitar uma resposta no teclado.

# A resposta que o usuário digitar será guardada na caixa 'linguagem_favorita'.

# Depois, o computador mostra o que ele acabou de escutar e guardar.

# ==============================================================================
# DESAFIO 7: O Formulário de Transporte
# ==============================================================================
# CONCEITO: Praticando a coleta de dados (input). Todo sistema precisa receber 
# dados de alguém (do teclado, do mouse, da tela do celular).



# ==============================================================================
# DESAFIO 8: Mudança de Planos
# ==============================================================================
# CONCEITO: Por que se chama "Variável"? Porque o valor pode VARIAR! 
# Se você colocar algo novo em uma caixa que já estava cheia, o conteúdo antigo 
# é jogado fora e substituído pelo novo.

# A caixa recebe o valor "Estágio".


# A MESMA caixa agora recebe o valor "Full Stack". O "Estágio" sumiu para sempre.


# ==============================================================================
# DESAFIO 9: Avaliação de Perfil
# ==============================================================================
# CONCEITO: "Booleanos" (True ou False) são como interruptores de luz: Ligado ou Desligado,
# Sim ou Não, Verdadeiro ou Falso. 
# Importante: Em Python, eles PRECISAM começar com letra maiúscula (True / False) e não usam aspas.





# ==============================================================================
# DESAFIO 10: O Grito do Diretor
# ==============================================================================
# CONCEITO: Textos em Python possuem "ferramentas" embutidas chamadas de "métodos".
# O método '.upper()' (do inglês "upper case" = letra maiúscula) pega qualquer 
# texto minúsculo e transforma em maiúsculo na hora de exibir.



# ==============================================================================
# DESAFIO 11: A Senha de Acesso
# ==============================================================================
# CONCEITO: A função 'len()' vem da palavra "length" (comprimento/tamanho em inglês).
# Ela serve para o computador contar quantos caracteres (letras, números, espaços) 
# existem dentro de um texto.



# A senha tem a palavra "senha" (5 letras) + "123" (3 números) = 8 caracteres.

# ==============================================================================
# DESAFIO 12: Juntando os Pedaços
# ==============================================================================
# CONCEITO: Ao "colar" (concatenar) variáveis de texto usando o sinal de mais (+), 
# o computador junta tudo exatamente do jeito que está. Se você não colocar um 
# espaço manualmente (" "), as palavras ficarão grudadas ("ArthurSilva").


# Juntando: "Arthur" + " " (espaço vazio) + "Silva" = "Arthur Silva"


# ==============================================================================
# DESAFIO 13: Cálculo do Benefício
# ==============================================================================
# CONCEITO: O sinal de mais (+) é inteligente. 
# - Se as variáveis forem TEXTOS (com aspas), ele junta as palavras.
# - Se as variáveis forem NÚMEROS (sem aspas), ele faz a conta de matemática (soma).


# Aqui ele entende que é matemática, então 2000 + 150 vira 2150.


# ==============================================================================
# DESAFIO 14: O Bug do Código
# ==============================================================================
# CONCEITO: O computador é burro e obedece regras estritas. Texto SEMPRE precisa 
# de aspas (duplas "" ou simples ''). Se você não colocar, o computador acha que as 
# palavras são comandos ou variáveis que não existem, causando um "Erro de Sintaxe".

# CORREÇÃO: O texto informativo precisa estar envolto em aspas.


# ==============================================================================
# DESAFIO 15: O Relatório de Fim de Dia (Projeto Final da Aula)
# ==============================================================================
# CONCEITO: Aqui juntamos tudo o que aprendemos e introduzimos a 'f-string'.
# Colocar um 'f' minúsculo antes das aspas de um print (f"...") permite "injetar" 
# as nossas caixinhas (variáveis) diretamente no meio do texto, apenas colocando-as 
# entre chaves { }. É muito mais fácil do que usar o símbolo de mais (+).



# EXPLICAÇÃO: Em vez de fazer print("Nome: " + nome + ", Idade: " + idade...), 
# usamos a formatação 'f-string' para deixar o código limpo e elegante!
