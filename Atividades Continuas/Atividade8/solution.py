# Como embasamento utilizei a solução e explicação apresentada em:
# https://programmerall.com/article/40731413696/

def main():
    with open("input.txt", "r") as f:
        lines = [line.strip() for line in f if line.strip() != ""]

    idx = 0  # índice para percorrer as linhas lidas
    while idx < len(lines):
        parts = lines[idx].split()
        idx += 1
        n = int(parts[0])
        m = int(parts[1])
        # Se n+m for  encerra (caso de teste final)
        if n + m == 0:
            break

        # --- Inicialização dos vetores de cobertura ---
        # st[i] é a máscara que representa o vértice i e seus vizinhos (a estação em i cobre i e seus adjacentes)
        # Inicialmente, cada vértice cobre a si mesmo.
        st = [(1 << i) for i in range(n)]
        
        # Lê as m arestas e atualiza as máscaras 
        for _ in range(m):
            a, b = map(int, lines[idx].split())
            idx += 1
            # Ajusta para índices 0-based.
            a -= 1
            b -= 1
            st[a] |= (1 << b)
            st[b] |= (1 << a)
        
        # --- Construção do vetor l ---
        # l[i] é a união (OR) de st[i], st[i+1], ..., st[n-1]. Essa informação serve para poda durante o backtracking.
        l_arr = [0] * n
        l_arr[n - 1] = st[n - 1]
        for i in range(n - 2, -1, -1):
            l_arr[i] = st[i] | l_arr[i + 1]
        
        full_mask = (1 << n) - 1  # máscara com todos os vértices cobertos

        # --- Função DFS (backtracking) ---
        # state: máscara atual de vértices cobertos
        # step: quantos vértices já foram selecionados
        # s: índice a partir do qual considerar novos vértices
        # maxlen: número máximo de estações que podemos escolher nessa tentativa
        def dfs(state, step, s, maxlen):
            # Se todos os vértices estão cobertos, retornamos True.
            if state == full_mask:
                return True
            # Se já usamos o número máximo de estações permitido sem cobrir todos, falha.
            if step == maxlen:
                return False
            # Se não há mais vértices para escolher, retorna False.
            if s >= n:
                return False

            # Percorre os vértices a partir do índice s
            for i in range(s, n):
                # Poda: se mesmo adicionando a cobertura de todos os vértices de i em diante
                # o estado não chega a cobrir todos, não vale a pena continuar.
                if (state | l_arr[i]) != full_mask:
                    break
                # Se adicionar a estação i não muda o estado (não adiciona cobertura nova), pula.
                if (state | st[i]) == state:
                    continue
                # Tenta incluir a estação em i e chama recursivamente.
                if dfs(state | st[i], step + 1, i + 1, maxlen):
                    return True
            return False

        # --- Busca pela solução mínima ---
        # Testa, progressivamente, se é possível cobrir todos os vértices com 1, 2, 3, ... estações.
        answer = None
        for maxlen in range(1, n + 1):
            if dfs(0, 0, 0, maxlen):
                answer = maxlen
                break

        print(answer)

if __name__ == '__main__':
    main()
