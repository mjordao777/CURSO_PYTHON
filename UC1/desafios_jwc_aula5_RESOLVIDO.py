# ==============================================================================
# CADERNO DE DESAFIOS RESOLVIDO (GABARITO) - AULA 5: OPERADORES LÓGICOS
# Empresa: JWC Tecnologia
# Módulo: Programador Full Stack - Processo Seletivo
# Perfil Técnico: Eduarda - Desenvolvedora Plena (Full Stack)
# ==============================================================================


# ==============================================================================
# DESAFIO 1: Validação de Acesso ao Módulo LMS (Operador 'and')
# ==============================================================================
idade = 20
matricula_ativa = True

if idade > 18 and matricula_ativa:
    print("Acesso liberado ao módulo avançado.")
else:
    print("Acesso negado: Requisitos não preenchidos.")


# ==============================================================================
# DESAFIO 2: Triagem de Mensagens no Chatbot (Operador 'or')
# ==============================================================================
mensagem_cliente = "Quero falar com o suporte"

if "suporte" in mensagem_cliente or "financeiro" in mensagem_cliente:
    print("Transferindo para um atendente humano...")
else:
    print("Atendimento automatizado em andamento.")


# ==============================================================================
# DESAFIO 3: Status de Manutenção do Sistema (Operador 'not')
# ==============================================================================
em_manutencao = False

if not em_manutencao:
    print("Servidor operacional. Iniciando rotina.")
else:
    print("Sistema em manutenção. Tente novamente mais tarde.")


# ==============================================================================
# DESAFIO 4: Emissão de Certificado de Conclusão (Operadores 'and' e 'not')
# ==============================================================================
nota_final = 8.5
possui_pendencia = False

if nota_final >= 7.0 and not possui_pendencia:
    print("Certificado emitido com sucesso!")
else:
    print("Emissão bloqueada. Verifique suas pendências ou nota.")


# ==============================================================================
# DESAFIO 5: Classificação de Desempenho do Código (if / elif / else com 'and')
# ==============================================================================
tempo_resposta_ms = 250

if tempo_resposta_ms < 100:
    print("Excelente performance.")
elif tempo_resposta_ms >= 100 and tempo_resposta_ms <= 300:
    print("Performance aceitável.")
else:
    print("Atenção: Código precisa de otimização!")


# ==============================================================================
# DESAFIO 6: Liberação de Bônus de Projeto (Operadores mistos 'or' e 'and')
# ==============================================================================
horas_extras = 15
projetos_entregues = 6
nota_avaliacao = 9.0

if horas_extras > 20 or (projetos_entregues > 5 and nota_avaliacao > 8.0):
    print("Colaborador elegível para bônus!")
else:
    print("Critérios de bônus não atingidos.")


# ==============================================================================
# DESAFIO 7: Validação de Cadastro de Usuário (Análise de Strings com 'and')
# ==============================================================================
usuario = "dev_python"

if len(usuario) > 3 and ' ' not in usuario:
    print("Nome de usuário válido!")
else:
    print("Nome de usuário inválido.")


# ==============================================================================
# DESAFIO 8: Menu de Feedback de Code Review (Match-Case)
# ==============================================================================
codigo_status = 2

match codigo_status:
    case 1:
        print("Aprovado: Código limpo e pronto para produção.")
    case 2:
        print("Aprovado com ressalvas: Ajustar nomes de variáveis.")
    case 3:
        print("Reprovado: Reescrever lógica e adicionar tratamento de erros.")
    case _:
        print("Status não identificado. Consulte a Eduarda.")


# ==============================================================================
# ==============================================================================
# DESAFIOS OPCIONAIS RESOLVIDOS (PARA ALUNOS AVANÇADOS)
# ==============================================================================
# ==============================================================================


# ==============================================================================
# DESAFIO 9 (OPCIONAL): Regra de Desconto em Checkout LMS
# ==============================================================================
ex_aluno = False
cupom_valido = True
is_black_friday = True

if ex_aluno or (cupom_valido and is_black_friday):
    print("Desconto de 20% aplicado!")
else:
    print("Valor integral da assinatura.")


# ==============================================================================
# DESAFIO 10 (OPCIONAL): Liberação de Feature Flag em Produção
# ==============================================================================
tipo_usuario = "beta_tester"
versao_sistema = 2.1

if (tipo_usuario == "beta_tester" or tipo_usuario == "admin") and versao_sistema >= 2.0:
    print("Nova funcionalidade habilitada.")
else:
    print("Funcionalidade indisponível nesta versão.")


# ==============================================================================
# DESAFIO 11 (OPCIONAL): Validação de Formulário Completo
# ==============================================================================
nome = "Ana"
email = "ana@jwc.com"

if (len(nome) > 0 and len(email) > 0) and ('@' in email):
    print("Formulário validado com sucesso!")
else:
    print("Preencha todos os campos corretamente.")


# ==============================================================================
# DESAFIO 12 (OPCIONAL): Filtro de Logs de Erro Críticos
# ==============================================================================
nivel_log = "CRITICAL"
ambiente = "PROD"

if (nivel_log == "ERROR" or nivel_log == "CRITICAL") and ambiente == "PROD":
    print("DISPARAR ALERTA NO SLACK DA EQUIPE!")
else:
    print("Log registrado sem necessidade de alerta urgente.")


# ==============================================================================
# DESAFIO 13 (OPCIONAL): Validação de Inscrição em Torneio de e-Sports
# ==============================================================================
idade = 18
ranking = "Mestre"
banido = False

if idade >= 16 and (ranking == "Diamante" or ranking == "Mestre") and not banido:
    print("Inscrição confirmada no torneio!")
else:
    print("Inscrição recusada por não atender aos requisitos.")


# ==============================================================================
# DESAFIO 14 (OPCIONAL): Refatoração de Código Confuso
# ==============================================================================
ativo = True
admin = True

# Versão refatorada e limpa:
if ativo and admin:
    print("Acesso total")


# ==============================================================================
# DESAFIO 15 (OPCIONAL): O Desafio Supremo de Pipeline da Eduarda
# ==============================================================================
testes_passaram = True
cobertura_codigo = 85
vulnerabilidade_alta = False

if testes_passaram and cobertura_codigo >= 80 and not vulnerabilidade_alta:
    print("Deploy aprovado pela Eduarda! Enviando para produção...")
else:
    print("Deploy bloqueado! Corrija os problemas apontados no relatório.")