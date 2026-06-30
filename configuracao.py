# ============================================
# Máquina de Turing que aceita L = {a^n b^n c^n | n >= 1}
# ============================================

alfabeto_entrada = ['a', 'b', 'c']
simbolos_auxiliares = ['X', 'Y', 'Z']

estados = ['q0', 'q1', 'q2', 'q3', 'q4', 'qAcc']
estado_inicial = 'q0'
estados_finais = ['qAcc']

transicoes = {
    # q0: Busca o primeiro 'a' não marcado. Ignora X e volta para o início
    ('q0', '*'): ('q0', '*', 'D'),
    ('q0', 'X'): ('q0', 'X', 'D'),
    ('q0', 'a'): ('q1', 'X', 'D'),
    ('q0', 'Y'): ('q4', 'Y', 'D'),

    # q1: Pula 'a's e 'Y's até achar o 'b'
    ('q1', 'a'): ('q1', 'a', 'D'),
    ('q1', 'Y'): ('q1', 'Y', 'D'),
    ('q1', 'b'): ('q2', 'Y', 'D'),

    # q2: Pula 'b's e 'Z's até achar o 'c'
    ('q2', 'b'): ('q2', 'b', 'D'),
    ('q2', 'Z'): ('q2', 'Z', 'D'),
    ('q2', 'c'): ('q3', 'Z', 'E'),

    # q3: Volta para o início da fita, atravessando TUDO o que encontrar
    ('q3', 'a'): ('q3', 'a', 'E'),
    ('q3', 'b'): ('q3', 'b', 'E'),
    ('q3', 'c'): ('q3', 'c', 'E'),
    ('q3', 'X'): ('q3', 'X', 'E'),
    ('q3', 'Y'): ('q3', 'Y', 'E'),
    ('q3', 'Z'): ('q3', 'Z', 'E'),
    ('q3', '*'): ('q0', '*', 'D'), # Chegou no início, volta para q0

    # q4: Confere se sobraram apenas Ys e Zs (se não há mais 'a's ou 'b's)
    ('q4', 'Y'): ('q4', 'Y', 'D'),
    ('q4', 'Z'): ('q4', 'Z', 'D'),
    ('q4', 'ε'): ('qAcc', 'ε', 'P')
}