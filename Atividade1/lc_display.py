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

def process_input(s, n):
    total_width = len(n) * (s + 3) - 1
    screen = [[" " for _ in range(total_width)] for _ in range(2 * s + 3)]

    for idx, number in enumerate(n):
        representation = segments[number]
        start_col = idx * (s + 3) 
        for rep in representation:
            if rep == 'top':
                for col in range(start_col + 1, start_col + s + 1):
                    screen[0][col] = "-"
            elif rep == 'top-left':
                for row in range(1, s + 1):
                    screen[row][start_col] = "|"
            elif rep == 'top-right':
                for row in range(1, s + 1):
                    screen[row][start_col + s + 1] = "|"
            elif rep == 'middle':
                for col in range(start_col + 1, start_col + s + 1):
                    screen[s + 1][col] = "-"
            elif rep == 'bottom-left':
                for row in range(s + 2, 2 * s + 2):
                    screen[row][start_col] = "|"
            elif rep == 'bottom-right':
                for row in range(s + 2, 2 * s + 2):
                    screen[row][start_col + s + 1] = "|"
            elif rep == 'bottom':
                for col in range(start_col + 1, start_col + s + 1):
                    screen[2 * s + 2][col] = "-"

    show_number(screen)

def show_number(screen):
    for row in screen:
        print("".join(row))

s, n = -1, ""

while not (s == 0 and n == "0"):
    s, n = input("Enter size and number (enter 0 0 to stop): ").split()
    s = int(s)
    if s == 0 and n == "0":
        break
    process_input(s, n)
