def calculate(n):
    divisor = 1 # Divisor inicial
    length = 1

    while divisor % n != 0:
        divisor = (divisor * 10 + 1) % n # Calculo para saber qual o proximo divisor 
        length += 1 

    return length

with open("input.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    n = int(line.strip()) 
    print(f"{calculate(n)}")
