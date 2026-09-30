# ==============================================================================
# CADERNO DE DESAFIOS - AULA 3: GIT E EXPRESSÕES ARITMÉTICAS
# Empresa: JWC Tecnologia
# Módulo: Programador Full Stack - Processo Seletivo
# ==============================================================================

# ==============================================================================
# DESAFIO 1: O Onboarding com a Tech Lead (O Mundo do GIT)
# ==============================================================================
# Situação: No seu primeiro dia focado em código, a Patrícia (Líder Técnica) 
# avisa que não aceita código perdido. Antes de você programar a regra de 
# negócio do cliente, ela quer garantir que você entende de versionamento.
# Enunciado: Faça uma breve pesquisa e responda (usando a função print):
# A) Quem criou o Git e o GitHub?[cite: 2]
# B) Para qual empresa o GitHub foi vendido e por qual valor aproximado?[cite: 2]
# C) Cite o nome de pelo menos dois outros subversionadores (concorrentes do GitHub) 
#    usados no mercado.[cite: 2]

# Código:


# ==============================================================================
# DESAFIO 2: O Padrão da Empresa (Comandos GIT)
# ==============================================================================
# Situação: A Patrícia criou um manual de boas práticas da JWC. Todo desenvolvedor 
# precisa saber o fluxo básico para salvar o código na nuvem e evitar desastres. 
# Enunciado: Sem usar código Python, escreva dentro de prints quais são os 
# comandos do GIT responsáveis por:
# 1. Iniciar um novo repositório local na sua máquina.[cite: 2]
# 2. Verificar o estado atual dos arquivos (o que foi alterado).[cite: 2]
# 3. Adicionar arquivos para a "área de preparação" para serem salvos.[cite: 2]
# 4. Salvar as alterações criando um ponto na história (com uma mensagem).[cite: 2]

# Código:


# ==============================================================================
# DESAFIO 3: A Primeira Feature (Operador de Subtração -)
# ==============================================================================
# Situação: O Arthur (Product Owner) chegou com uma demanda de um cliente da 
# área de educação[cite: 2]. O sistema precisa mostrar no painel da diretoria 
# quantas vagas ainda estão disponíveis na escola.
# Enunciado: Como desenvolvedor, crie uma variável 'capacidade_total_escola' 
# valendo 850. Crie 'alunos_matriculados' valendo 523. O sistema deve calcular 
# a variável 'vagas_disponiveis' subtraindo os matriculados da capacidade total. 
# Imprima o resultado na tela.

# Código:


# ==============================================================================
# DESAFIO 4: Calculando o Faturamento (Operador de Multiplicação *)
# ==============================================================================
# Situação: O Arthur (PO) pediu para você criar a funcionalidade que projeta o 
# faturamento do mês seguinte, multiplicando o número de alunos pela mensalidade.
# Enunciado: Crie a variável 'mensalidade_padrao' valendo 850.50. Crie a variável 
# 'novas_matriculas' valendo 42. Crie a variável 'faturamento_projetado' que 
# multiplique os dois valores e exiba o resultado para o cliente.

# Código:


# ==============================================================================
# DESAFIO 5: Divisão de Turmas (Operador de Divisão /)
# ==============================================================================
# Situação: O sistema precisa de um botão "Gerar Grupos de Estudo". O Arthur (PO) 
# definiu que a regra de negócio é dividir o total de alunos de uma turma pelo 
# tamanho ideal do grupo.
# Enunciado: Crie 'total_alunos_turma' valendo 45. Crie 'tamanho_grupo_ideal' 
# valendo 5. Calcule e imprima quantos grupos serão formados usando a divisão (/).
# (Note que no Python, a divisão normal sempre retorna um número quebrado - float).

# Código:


# ==============================================================================
# DESAFIO 6: Lógica de Paginação (Divisão Inteira // e Resto %)
# ==============================================================================
# Situação: O cliente educacional comprou 100 tablets. O sistema precisa 
# distribuir esses tablets igualmente entre 3 salas, mas a Patrícia (Tech Lead) 
# avisa: "O sistema não pode quebrar um tablet no meio!".
# Enunciado: Você precisa usar a divisão inteira (//) para descobrir quantos 
# tablets inteiros vão para cada sala. Depois, use o resto da divisão (%) para 
# programar a variável 'tablets_sobra' e avisar quantos ficam na reserva da TI. 
# Imprima ambos os resultados.

# Código:


# ==============================================================================
# DESAFIO 7: Escalabilidade de Servidor (Exponenciação **)
# ==============================================================================
# Situação: A Patrícia (Tech Lead) precisa configurar os servidores da AWS para 
# suportar o novo sistema educacional. Ela sabe que a base de dados dobra de 
# tamanho a cada ano.
# Enunciado: Crie a variável 'armazenamento_atual_tb' valendo 3. Como o volume 
# dobra anualmente, calcule o tamanho necessário para daqui a 4 anos elevando 
# 2 à 4ª potência (**). Multiplique o resultado pelo armazenamento atual e imprima.

# Código:


# ==============================================================================
# DESAFIO 8: O MVP do Boletim Digital (Projeto Final da Aula 3)
# ==============================================================================
# Situação: Sprint final! O Arthur (PO) precisa apresentar o Produto Mínimo 
# Viável (MVP) funcionando. A funcionalidade principal é o cálculo da média 
# do aluno pelo professor[cite: 2].
# Regra da Patrícia: "O sistema não pode ter valores fixos. O usuário (professor) 
# é quem deve digitar os dados no terminal."
# Enunciado: 
# 1. Use input() para capturar o nome do aluno.
# 2. Use input() para capturar as notas do 1º, 2º e 3º trimestre (lembre-se 
#    de aplicar a conversão float() para que o Python entenda como matemática).
# 3. Calcule a média somando as 3 notas e dividindo por 3. (Cuidado com a 
#    ordem de precedência matemática: use parênteses!).
# 4. Exiba o resultado formatado (f-string) na tela para o professor: 
#    "Sistema JWC: O aluno [nome] fechou o ano com média [media]".

# Código: