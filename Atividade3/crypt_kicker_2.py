def decrypt(file_input):
    # The known plaintext
    target_sentence = "the quick brown fox jumps over the lazy dog"
    target_lengths = [len(word) for word in target_sentence.split()]

    # Read input from the file
    with open(file_input, 'r') as file:
        lines = file.read().strip().split('\n')

    # Extract the number of test cases
    test_cases = int(lines[0])
    results = []
    index = 1

    # Process each test case
    for _ in range(test_cases):
        # Read encrypted lines for the current test case
        num_lines = 0
        while index + num_lines < len(lines) and lines[index + num_lines].strip():
            num_lines += 1

        encrypted_lines = lines[index:index + num_lines]
        index += num_lines + 1  # Move to the next test case

        # Try to find a matching line
        mapping = None
        for line in encrypted_lines:
            words = line.split()
            if [len(word) for word in words] == target_lengths:
                temp_mapping = {}
                reverse_mapping = {}
                valid = True

                # Try to create a mapping
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

        # Apply the mapping or output "No solution"
        if mapping:
            decrypted_lines = [
                "".join(mapping.get(c, c) for c in line)
                for line in encrypted_lines
            ]
            results.append("\n".join(decrypted_lines))
        else:
            results.append("No solution")

    # Print results to the console
    print("\n\n".join(results))


# Example usage
input_file = 'input.txt'
decrypt(input_file)
