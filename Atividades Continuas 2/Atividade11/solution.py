def main():
    with open("input.txt", "r") as f:
        data = f.read().split()
    idx = 0
    results = []
    
    # Processa cada caso de teste até o final dos dados
    while idx < len(data):
        m = int(data[idx])
        n = int(data[idx+1])
        idx += 2
        matrix = []
        for _ in range(m):
            row = list(map(int, data[idx:idx+n]))
            matrix.append(row)
            idx += n
        
        dp = [[0] * n for _ in range(m)]
        nxt = [[0] * n for _ in range(m)]
        
        # Inicializa a última coluna
        for i in range(m):
            dp[i][n-1] = matrix[i][n-1]
        
        # Preenche a tabela de DP de trás para frente
        for j in range(n-2, -1, -1):
            for i in range(m):
                neighbors = [ (i-1) % m, i, (i+1) % m ]
                neighbors.sort()  # Garante a ordem lexicográfica
                best = float('inf')
                best_neighbor = 0
                for v in neighbors:
                    if dp[v][j+1] < best:
                        best = dp[v][j+1]
                        best_neighbor = v
                dp[i][j] = matrix[i][j] + best
                nxt[i][j] = best_neighbor
        
        # Seleciona a linha inicial que minimiza dp[i][0]
        min_cost = float('inf')
        start = 0
        for i in range(m):
            if dp[i][0] < min_cost:
                min_cost = dp[i][0]
                start = i
        
        # Reconstrução do caminho
        path = []
        i = start
        for j in range(n):
            path.append(str(i+1))  # Converte para 1-index
            if j < n-1:
                i = nxt[i][j]
        
        results.append(" ".join(path))
        results.append(str(min_cost))
    
    print("\n".join(results))

if __name__ == '__main__':
    main()
