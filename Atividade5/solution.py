def calculate(n):
    divisor = 1 
    length = 1

    while divisor % n != 0:
        divisor = (divisor * 10 + 1) % n 
        length += 1 

    return length

with open("input.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    n = int(line.strip()) 
    print(f"{calculate(n)}")
