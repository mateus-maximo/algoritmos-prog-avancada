# A ideia é dividir o desenho do dígito em segmentos
# Existem 3 segmentos horizontais (topo, meio e base) e 4 segmentos verticais (superior-esquerdo, superior-direito, inferior-esquerdo e inferior-direito)
# O número 8 possui todos os segmentos
segments = {
    '0': ['top', 'top-left', 'top-right', 'bottom-left', 'bottom-right', 'bottom'],
    '1': ['top-right', 'bottom-right'],
    '2': ['top', 'top-right', 'middle', 'bottom-left', 'bottom'],
    '3': ['top', 'top-right', 'middle', 'bottom-right', 'bottom'],
    '4': ['top-left', 'top-right', 'middle', 'bottom-right'],
    '5': ['top', 'top-left', 'middle', 'bottom-right', 'bottom'],
    '6': ['top', 'top-left', 'middle', 'bottom-left', 'bottom-right', 'bottom'],
    '7': ['top', 'top-right', 'bottom-right'],
    '8': ['top', 'top-left', 'top-right', 'middle', 'bottom-left', 'bottom-right', 'bottom'],
    '9': ['top', 'top-left', 'top-right', 'middle', 'bottom-right', 'bottom'],
}

# Função para exibir o número formatado na tela
def show_number(screen):
    for row in screen:
        print("".join(row))

# Função que processa o tamanho e o número fornecido como entrada
def process_input(s, n):
    # Cada dígito ocupa (s + 3) colunas
    # -1 porque o último dígito não exige espaço extra no final
    total_width = len(n) * (s + 3) - 1
    
    # A ideia é representar o número inteiro como uma matriz
    screen = [[" " for _ in range(total_width)] for _ in range(2 * s + 3)]

    for idx, number in enumerate(n):
        representation = segments[number]
        start_col = idx * (s + 3) 
        for segment in representation:
            if segment == 'top':
                for col in range(start_col + 1, start_col + s + 1):
                    screen[0][col] = "-"
            elif segment == 'top-left':
                for row in range(1, s + 1):
                    screen[row][start_col] = "|"
            elif segment == 'top-right':
                for row in range(1, s + 1):
                    screen[row][start_col + s + 1] = "|"
            elif segment == 'middle':
                for col in range(start_col + 1, start_col + s + 1):
                    screen[s + 1][col] = "-"
            elif segment == 'bottom-left':
                for row in range(s + 2, 2 * s + 2):
                    screen[row][start_col] = "|"
            elif segment == 'bottom-right':
                for row in range(s + 2, 2 * s + 2):
                    screen[row][start_col + s + 1] = "|"
            elif segment == 'bottom':
                for col in range(start_col + 1, start_col + s + 1):
                    screen[2 * s + 2][col] = "-"

    show_number(screen)

s, n = -1, ""

# Loop para receber entradas do usuário até que '0 0' seja fornecido
while not (s == 0 and n == "0"):
    s, n = input("Enter size and number (enter 0 0 to stop): ").split()
    s = int(s)
    if s == 0 and n == "0":
        break
    process_input(s, n)
