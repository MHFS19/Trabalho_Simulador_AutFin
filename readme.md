# Simulador de Autômatos Finitos

## Descrição do Projeto
Este trabalho implementa um simulador de autômatos finitos determinísticos (DFA) e não-determinísticos (NFA) que:
- Processa arquivos de especificação de autômatos em formato JSON
- Executa testes a partir de arquivos CSV
- Gera relatórios de saída com métricas de desempenho

## Funcionalidades Principais
1. **Leitura de Autômatos**:
   - Suporte a estados inicial e finais
   - Processamento de transições (incluindo ε-transições)
   - Validação da estrutura do autômato

2. **Simulação**:
   - Processamento de cadeias de entrada
   - Detecção de aceitação/rejeição
   - Cálculo do tempo de execução por teste

3. **Geração de Relatórios**:
   - Saída em formato CSV
   - Comparação entre resultados esperados e obtidos
   - Registro de tempo de processamento

## Estrutura do Projeto
 # Código principal
 # Validação de arquivos de entrada
 # Funções auxiliares
 # Exemplos de arquivos
 # Exemplo de autômato
 # Exemplo de casos de teste

 # Exemplo de uso (saída)
 palavra de entrada;resultadoesperado;resultado_obtido;tempo
 ab;1;1;0.000456
 aab;0;0;0.000321
 bbb;1;0;0.000289
