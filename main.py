from maquina_turing import MaquinaTuring
import configuracao as cfg

def main():
    # Instanciando, dados importados do arquivo configuracao.py
    mt = MaquinaTuring(
        alfabeto=cfg.alfabeto_entrada,
        auxiliares=cfg.simbolos_auxiliares,
        estados=cfg.estados,
        estado_inicial=cfg.estado_inicial,
        estados_finais=cfg.estados_finais,
        transicoes=cfg.transicoes
    )

    mt.imprimir_definicao_formal()

    while True:
        print("\n==============================")
        palavra = input("Palavra para testar (ou digite 'sair' para encerrar): ")
        
        if palavra.lower() == 'sair':
            print("Encerrando o simulador. Até logo!")
            break
            
        palavra_valida = True
        
        for letra in palavra:
            if letra not in mt.alfabeto:
                print(f"ERRO: O símbolo '{letra}' não pertence ao alfabeto Σ.")
                palavra_valida = False
                break
                
        if not palavra_valida:
            continue

        mt.inicializar_fita(palavra)

        print("\n====== EXECUÇÃO ======")
        mt.executar()


if __name__ == "__main__":
    main()