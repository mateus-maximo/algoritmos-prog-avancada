def decrypt(file_input):
    """
    Função para decifrar o texto de entrada usando um mapeamento baseado em uma frase conhecida.
    """
    # O texto conhecido
    target_sentence = "the quick brown fox jumps over the lazy dog"
    target_lengths = [len(word) for word in target_sentence.split()]

    # Lê a entrada do arquivo
    with open(file_input, 'r') as file:
        lines = file.read().strip().split('\n')

    # Extrai o número de casos de teste
    test_cases = int(lines[0])
    results = []
    index = 1

    # Processa cada caso de teste
    for _ in range(test_cases):
        # Lê as linhas criptografadas para o caso de teste atual
        num_lines = 0
        while index + num_lines < len(lines) and lines[index + num_lines].strip():
            num_lines += 1

        encrypted_lines = lines[index:index + num_lines]
        index += num_lines + 1  # Avança para o próximo caso de teste

        # Tenta encontrar uma linha correspondente
        mapping = None
        for line in encrypted_lines:
            words = line.split()
            if [len(word) for word in words] == target_lengths:
                temp_mapping = {}
                reverse_mapping = {}
                valid = True

                # Tenta criar um mapeamento
                for enc_word, target_word in zip(words, target_sentence.split()):
                    for enc_char, target_char in zip(enc_word, target_word):
                        if enc_char in temp_mapping:
                            if temp_mapping[enc_char] != target_char:
                                valid = False
                                break
                        elif target_char in reverse_mapping:
                            if reverse_mapping[target_char] != enc_char:
                                valid = False
                                break
                        else:
                            temp_mapping[enc_char] = target_char
                            reverse_mapping[target_char] = enc_char

                    if not valid:
                        break

                if valid:
                    mapping = temp_mapping
                    break

        # Aplica o mapeamento ou exibe "No solution"
        if mapping:
            decrypted_lines = [
                "".join(mapping.get(c, c) for c in line)
                for line in encrypted_lines
            ]
            results.append("\n".join(decrypted_lines))
        else:
            results.append("No solution")

    # Exibe os resultados no console
    print("\n\n".join(results))


# Exemplo de uso
input_file = 'input.txt'
decrypt(input_file)
