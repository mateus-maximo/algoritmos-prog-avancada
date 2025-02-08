"""
Para resolver o problema, a solução utiliza os seguintes passos:
1. Fatoração de m: o número m é decomposto em fatores primos (por exemplo, 72 = 2^3 * 3^2).
2. Fórmula de Legendre: para cada primo p presente na fatoração de m, usamos a fórmula de Legendre
   para contar quantas vezes p divide n!:
       expoente_p(n!) = ⌊n/p⌋ + ⌊n/p²⌋ + ⌊n/p³⌋ + ...
3. Verificação: se para algum primo p o expoente em n! for menor que o expoente requerido em m,
   então m não divide n!. Caso contrário, m divide n!.

Referências:
------------
- Ideia foi retirada daqui: https://algorithmist.com/wiki/UVa_10139_-_Factovisors
- Discussões e soluções similares encontradas em fóruns de programação competitiva.
"""

def sieve(n):
    """Retorna uma lista de números primos até n (inclusivo)."""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i, prime in enumerate(is_prime) if prime]

def factorize(m, primes):
    """
    Fatora o número m em seus fatores primos.
    Retorna um dicionário {primo: expoente}.
    """
    factors = {}
    temp = m
    for p in primes:
        if p * p > temp:
            break
        if temp % p == 0:
            count = 0
            while temp % p == 0:
                count += 1
                temp //= p
            factors[p] = count
        if temp == 1:
            break
    if temp > 1:
        factors[temp] = factors.get(temp, 0) + 1
    return factors

def exponent_in_factorial(n, p):
    """
    Conta o expoente do primo p em n! usando a fórmula de Legendre.
    """
    count = 0
    power = p
    while power <= n:
        count += n // power
        power *= p
    return count

def process_case(n, m, primes):
    """
    Retorna True se m divide n!, caso contrário, retorna False.
    """
    # Caso especial: m == 0 (divisão por zero é indefinida)
    if m == 0:
        return False
    # 1 divide qualquer número.
    if m == 1:
        return True
    # Para n = 0 ou 1, n! = 1, então apenas m == 1 divide.
    if n < 2:
        return m == 1

    # Fatora m.
    factors = factorize(m, primes)
    # Para cada fator primo, n! deve ter pelo menos o mesmo expoente que m exige.
    for p, required_exp in factors.items():
        if exponent_in_factorial(n, p) < required_exp:
            return False
    return True

def main():
    # Pré-computa os primos até 50000. Isso é suficiente para fatorar m (m está no intervalo de 32 bits).
    primes = sieve(50000)
    
    # Abre o arquivo de entrada.
    with open("input.txt", "r") as fin:
        for line in fin:
            line = line.strip()
            if not line:
                continue  # ignora linhas em branco
            parts = line.split()
            if len(parts) < 2:
                continue  # ignora linhas inválidas
            try:
                n = int(parts[0])
                m = int(parts[1])
            except ValueError:
                continue  # ignora linhas com valores não inteiros

            # Guarda o valor original de m para impressão.
            original_m = m

            # Determina se m divide n!
            if process_case(n, m, primes):
                print(f"{original_m} divides {n}!")
            else:
                print(f"{original_m} does not divide {n}!")

if __name__ == '__main__':
    main()
