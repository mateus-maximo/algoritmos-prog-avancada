def solve_slash_maze(maze_list):
    # Lista que armazenará as linhas de saída formatadas para cada caso
    output_lines = []
    maze_number = 1  # Contador para numerar os labirintos na saída

    # Processa cada caso de teste
    for w, h, lines in maze_list:
        # Calcula as dimensões da grade expandida (3 vezes maior que o original)
        H, W = 3 * h, 3 * w
        # Inicializa a grade expandida com zeros (0 = espaço livre)
        grid = [[0] * W for _ in range(H)]
        
        # Expande o labirinto original para a grade 3x3
        for i in range(h):
            for j, ch in enumerate(lines[i]):
                if ch == '/':
                    # Marca as posições que formam a parede para '/'
                    grid[3 * i + 0][3 * j + 2] = 1
                    grid[3 * i + 1][3 * j + 1] = 1
                    grid[3 * i + 2][3 * j + 0] = 1
                elif ch == '\\':
                    # Marca as posições que formam a parede para '\'
                    grid[3 * i + 0][3 * j + 0] = 1
                    grid[3 * i + 1][3 * j + 1] = 1
                    grid[3 * i + 2][3 * j + 2] = 1

        # Cria uma matriz para acompanhar as células já visitadas
        visited = [[False] * W for _ in range(H)]
        cycle_count = 0  # Contador de ciclos fechados
        longest_cycle = 0  # Comprimento do maior ciclo encontrado
        # Define os movimentos ortogonais (cima, baixo, esquerda, direita)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Percorre cada célula da grade expandida
        for r in range(H):
            for c in range(W):
                # Se a célula é livre e não foi visitada, inicia uma DFS
                if grid[r][c] == 0 and not visited[r][c]:
                    stack = [(r, c)]
                    visited[r][c] = True
                    is_cycle = True  # Supomos inicialmente que a região é um ciclo
                    region_size = 0  # Contador para o tamanho da região conectada

                    # Executa a DFS utilizando uma pilha
                    while stack:
                        rr, cc = stack.pop()
                        region_size += 1  # Incrementa o tamanho da região
                        # Se a célula toca a borda, a região não é um ciclo fechado
                        if rr == 0 or rr == H - 1 or cc == 0 or cc == W - 1:
                            is_cycle = False
                        # Verifica os vizinhos nas 4 direções
                        for dr, dc in directions:
                            nr, nc = rr + dr, cc + dc
                            if 0 <= nr < H and 0 <= nc < W:
                                if grid[nr][nc] == 0 and not visited[nr][nc]:
                                    visited[nr][nc] = True
                                    stack.append((nr, nc))
                    # Se a região não tocou a borda, é um ciclo fechado
                    if is_cycle:
                        cycle_count += 1
                        # O tamanho do ciclo é o número de células livres dividido por 3
                        cycle_length = region_size // 3
                        if cycle_length > longest_cycle:
                            longest_cycle = cycle_length

        # Formata a saída para o caso atual
        output_lines.append(f"Maze #{maze_number}:")
        if cycle_count == 0:
            output_lines.append("There are no cycles.")
        else:
            output_lines.append(f"{cycle_count} Cycles; the longest has length {longest_cycle}.")
        output_lines.append("")  # Linha em branco entre os casos
        maze_number += 1

    return output_lines

def main():
    # Abre o arquivo "input.txt" e lê todas as linhas não vazias, removendo espaços finais
    with open("input.txt", "r") as f:
        lines = [line.rstrip() for line in f if line.rstrip() != ""]

    maze_list = []
    i = 0
    # Processa a entrada, lendo cada caso de teste
    while i < len(lines):
        parts = lines[i].split()
        w, h = int(parts[0]), int(parts[1])
        # Termina o processamento se w e h forem zero
        if w == 0 and h == 0:
            break
        i += 1
        maze = []
        # Lê as h linhas que compõem o labirinto
        for _ in range(h):
            maze.append(lines[i])
            i += 1
        maze_list.append((w, h, maze))
    
    # Processa todos os casos de teste e obtém as linhas de saída formatadas
    result = solve_slash_maze(maze_list)
    # Imprime o resultado para cada linha
    for line in result:
        print(line)

if __name__ == "__main__":
    main()
