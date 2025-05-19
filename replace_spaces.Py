def replace_spaces_with_commas_and_quotes(text):
    words = text.split(' ')

    # Add quotes around each word
    quoted_words = [f'"{word}"' for word in words]

    # Join the words with commas
    result = ','.join(quoted_words)

    return result

input_text = "CGCCCCTCTCGGGGGTGTTCAGTAACCGGCCA GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG TAGTACCGAGACCGAAAGAAGTATACAGGCGT TAGATCAAGTTTCAGGTGCACGTCGGTGAACC AATCCACCAGCTCCACGTGCAATGTTGGCCTA"
output_text = replace_spaces_with_commas_and_quotes(input_text)
print(output_text)
