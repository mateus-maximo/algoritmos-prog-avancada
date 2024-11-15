# The idea is to break the drawing of the digit into segments
# There are 3 horizontal segments (top, middle, and bottom) and 4 vertical segments (top-left, top-right, bottom-left, and bottom-right)
# The number 8 has all segments
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

def show_number(screen):
    for row in screen:
        print("".join(row))

def process_input(s, n):
    # Each digit occupies (s + 3) columns
    # -1 because the last digit does not require extra space at the end
    total_width = len(n) * (s + 3) - 1
    
    # The idea is to represent the whole number as a matrix
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

while not (s == 0 and n == "0"):
    s, n = input("Enter size and number (enter 0 0 to stop): ").split()
    s = int(s)
    if s == 0 and n == "0":
        break
    process_input(s, n)
