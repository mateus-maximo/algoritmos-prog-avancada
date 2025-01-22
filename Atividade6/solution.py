"""
Este programa resolve o problema de contar o número de expressões válidas de parênteses
com comprimento 'length' e profundidade máxima 'depth', considerando que:

- Uma expressão válida é formada por pares de parênteses balanceados.
- A profundidade máxima é definida pelo número máximo de níveis aninhados de parênteses.

Para resolver o problema:
1. A função `depthLowerSum` calcula o número de expressões com uma profundidade menor ou igual a `depth`.
2. Usamos recursão com memorização (tabela `memo`) para armazenar resultados previamente calculados,
   o que reduz a complexidade e acelera a execução.
3. No final, subtraímos as expressões com profundidade máxima `<= depth - 1` para obter as que
   atingem exatamente a profundidade `depth`.

Entrada:
- Comprimento da expressão (length) e profundidade máxima (depth).
- O comprimento deve ser par, pois cada `(` deve ter um `)` correspondente.

Saída:
- O número de expressões válidas que atingem exatamente a profundidade máxima especificada.
"""
def depthLowerSum(pairs, depth, memo):
    '''
    Calcula o número de expressões válidas com profundidade menor ou igual a `depth`
    '''
    if memo[pairs][depth] != -1:
        return memo[pairs][depth]
    if pairs == 0 or depth == 1:
        memo[pairs][depth] = 1
        return 1
    s = 0
    for i in range(pairs):
        s += depthLowerSum(i, depth - 1, memo) * \
            depthLowerSum(pairs - 1 - i, depth, memo)
    memo[pairs][depth] = s
    return s

if __name__ == '__main__':
    N, D = 161, 161 # So para criar uma tabela de memoizacao grande
    memo = [[-1] * D for _ in range(N)]

    print("Digite os valores de length e depth (Ctrl+D para encerrar):")
    while True:
        try:
            # Lendo os valores de entrada
            line = input().strip()
            if not line:
                break
            length, depth = map(int, line.split())
            pairs = length // 2
            # Calculando o número de expressões válidas com profundidade exata
            result = depthLowerSum(pairs, depth, memo) - depthLowerSum(pairs, depth - 1, memo)
            print(result)
        except EOFError:
            break
