import json
import csv
import time
import os

def main():
    automato_path = "automato.aut"
    testes_path = "testes.in"
    saida_path = "saida.out"

    try:
        if not os.path.exists(automato_path):
            raise FileNotFoundError(f"Arquivo do autômato não encontrado: {automato_path}")
        
        with open(automato_path, 'r') as f:
            automaton = json.load(f)

        if not os.path.exists(testes_path):
            raise FileNotFoundError(f"Arquivo de testes não encontrado: {testes_path}")
        
        test_cases = []
        with open(testes_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and ';' in line:
                    parts = line.split(';')
                    if len(parts) >= 2:
                        try:
                            test_cases.append((parts[0].strip(), int(parts[1].strip())))
                        except ValueError:
                            print(f"Aviso: Linha ignorada - formato inválido: {line}")

        if not test_cases:
            raise ValueError("Nenhum caso de teste válido encontrado")

        results = []
        for input_str, expected in test_cases:
            start_time = time.perf_counter()
            result = simulate(automaton, input_str)
            elapsed = time.perf_counter() - start_time
            results.append((input_str, expected, result, elapsed))

        os.makedirs(os.path.dirname(saida_path) or '.', exist_ok=True)

        with open(saida_path, 'w', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(['palavra de entrada', 'resultadoesperado', 'resultado_obtido', 'tempo'])
            for case in results:
                writer.writerow([
                    case[0],
                    case[1],
                    1 if case[2] else 0,
                    f"{case[3]:.6f}"
                ])
        print(f"Sucesso! Arquivo de saída criado em: {os.path.abspath(saida_path)}")

    except Exception as e:
        print(f"Erro: {str(e)}")

def simulate(automaton, input_str):
    current_state = automaton['initial']
    final_states = set(automaton['final'])
    transition_table = build_transition_table(automaton['transitions'])

    for symbol in input_str:
        if (current_state, symbol) in transition_table:
            current_state = transition_table[(current_state, symbol)]
        else:
            return False
    return current_state in final_states

def build_transition_table(transitions):
    table = {}
    for trans in transitions:
        key = (trans['from'], trans['read'])
        table[key] = trans['to']
    return table

if __name__ == '__main__':
    main()
