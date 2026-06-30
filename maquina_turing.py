class MaquinaTuring:
    def __init__(self, alfabeto, auxiliares, estados, estado_inicial, estados_finais, transicoes):
        self.alfabeto = alfabeto
        self.auxiliares = auxiliares
        self.estados = estados
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais
        self.transicoes = transicoes

        self.branco = "ε"
        self.inicio = "*"
        
        self.gama_permitido = set(self.alfabeto) | set(self.auxiliares) | {self.branco, self.inicio}

        self.fita = []
        self.cabeca = 0
        self.estado_atual = ""

    def imprimir_definicao_formal(self):
        print("\n--- Definição Formal da Máquina ---")
        print("M = (Q, Σ, Γ, δ, q0, F)")
        print(f"Q (Estados) = {{{', '.join(sorted(self.estados))}}}")
        print(f"Σ (Alfabeto de Entrada) = {{{', '.join(sorted(self.alfabeto))}}}")
        print(f"Γ (Alfabeto da Fita) = {{{', '.join(sorted(self.gama_permitido))}}}")
        print(f"q0 (Estado Inicial) = {self.estado_inicial}")
        print(f"F (Estados Finais) = {{{', '.join(sorted(self.estados_finais))}}}")
        print("δ (Transições configuradas):")
        for (est, lid), (nov, esc, mv) in self.transicoes.items():
            print(f"  δ({est}, {lid}) = ({nov}, {esc}, {mv})")
        print("-----------------------------------\n")

    def inicializar_fita(self, palavra):
        self.fita = [self.inicio] + list(palavra) + [self.branco] * 20
        self.cabeca = 0
        self.estado_atual = self.estado_inicial

    def mostrar_fita(self):
        print(f"\nEstado Atual: {self.estado_atual}")
        fita_formatada = ""
        for i, simbolo in enumerate(self.fita):
            if i == self.cabeca:
                fita_formatada += f"[{simbolo}] " 
            else:
                fita_formatada += f"{simbolo} "
        print(f"Fita: {fita_formatada.strip()}\n")

    def executar(self):
        passo = 1
        MAX_PASSOS = 1000 

        while passo <= MAX_PASSOS:
            if self.cabeca >= len(self.fita):
                self.fita.append(self.branco)

            if self.cabeca < 0:
                print("\nERRO FATAL: O cabeçote tentou mover para antes do início da fita.")
                print(">>> RESULTADO: PALAVRA REJEITADA <<<")
                return False

            self.mostrar_fita()

            simbolo = self.fita[self.cabeca]
            chave = (self.estado_atual, simbolo)

            if chave not in self.transicoes:
                print("--------------------------------")
                print(f"Nenhuma transição encontrada para δ({self.estado_atual}, {simbolo}).")
                print("\n>>> RESULTADO: PALAVRA REJEITADA <<<")
                return False

            novo_estado, escrever, movimento = self.transicoes[chave]
            print(f"Passo {passo} | δ({self.estado_atual}, {simbolo}) = ({novo_estado}, {escrever}, {movimento})")

            self.fita[self.cabeca] = escrever

            if movimento == "D":
                self.cabeca += 1
            elif movimento == "E":
                self.cabeca -= 1

            self.estado_atual = novo_estado

            if self.estado_atual in self.estados_finais:
                self.mostrar_fita()
                print("==============================")
                print(">>> RESULTADO: PALAVRA ACEITA <<<")
                print("==============================")
                return True

            passo += 1

        print(f"\nERRO: Loop infinito detectado! A máquina atingiu o limite de {MAX_PASSOS} passos.")
        print(">>> RESULTADO: PALAVRA REJEITADA <<<")
        return False