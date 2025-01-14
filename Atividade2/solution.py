def decrypt_phrase(words, index, mapping):
    """
    Tenta recursivamente decifrar a frase encontrando um mapeamento consistente.
    """
    if index == len(words):
        return mapping 

    word = words[index]
    for dict_word in [w for w in dictionary if len(w) == len(word)]:
        extended_mapping = mapping.copy()
        if is_mapping_consistent(word, dict_word, extended_mapping):
            result = decrypt_phrase(words, index + 1, extended_mapping)
            if result is not None:
                return result
    return None 

def is_mapping_consistent(encrypted_word, dict_word, mapping):
    """
    Verifica se 'encrypted_word' pode ser mapeada para 'dict_word' usando um cifrador de substituição,
    mantendo a consistência com o 'mapping' existente.
    """
    for c_enc, c_dict in zip(encrypted_word, dict_word):
        if c_enc in mapping:
            if mapping[c_enc] != c_dict:
                return False  # Mapeamento inconsistente
        else:
            if c_dict in mapping.values():
                return False  # Violação de mapeamento um-para-um
            mapping[c_enc] = c_dict
    return True

# Abre o arquivo de entrada
with open("test.txt", "r") as file:
    # Lê o número de palavras do dicionário
    num_words = int(file.readline().strip())

    # Lê as palavras do dicionário
    dictionary = [file.readline().strip() for _ in range(num_words)]

    # Lê o restante das linhas como frases
    phrases = [line.strip() for line in file]

# Processa cada frase
for phrase in phrases:
    words = phrase.split()
    mapping = {}
    result = decrypt_phrase(words, 0, mapping)
    if result is not None:
        # Decifra a frase usando o mapeamento
        decrypted_phrase = []
        for word in words:
            decrypted_word = ''.join(result.get(c, '*') for c in word)
            decrypted_phrase.append(decrypted_word)
        print(' '.join(decrypted_phrase))
    else:
        # Substitui todas as letras por '*'
        decrypted_phrase = ['*' * len(word) for word in words]
        print(' '.join(decrypted_phrase))
