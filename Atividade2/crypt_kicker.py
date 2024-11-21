def decrypt_phrase(words, index, mapping):
    """
    Recursively attempts to decrypt the phrase by finding a consistent mapping.
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
    Checks if 'encrypted_word' can be mapped to 'dict_word' using a substitution cipher,
    while maintaining consistency with the existing 'mapping'.
    """
    for c_enc, c_dict in zip(encrypted_word, dict_word):
        if c_enc in mapping:
            if mapping[c_enc] != c_dict:
                return False  # Inconsistent mapping
        else:
            if c_dict in mapping.values():
                return False  # One-to-one mapping violation
            mapping[c_enc] = c_dict
    return True

with open("test2.txt", "r") as file:
    # Read the number of dictionary words
    num_words = int(file.readline().strip())

    # Read the dictionary words
    dictionary = [file.readline().strip() for _ in range(num_words)]

    # Read the remaining lines as phrases
    phrases = [line.strip() for line in file]

# Process each phrase
for phrase in phrases:
    words = phrase.split()
    mapping = {}
    result = decrypt_phrase(words, 0, mapping)
    if result is not None:
        # Decipher the phrase using the mapping
        decrypted_phrase = []
        for word in words:
            decrypted_word = ''.join(result.get(c, '*') for c in word)
            decrypted_phrase.append(decrypted_word)
        print(' '.join(decrypted_phrase))
    else:
        # Replace all letters with '*'
        decrypted_phrase = ['*' * len(word) for word in words]
        print(' '.join(decrypted_phrase))
