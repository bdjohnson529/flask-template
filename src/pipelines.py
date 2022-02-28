def count_frequencies(input_string):
    lower = input_string.lower()

    char_freq = {}

    for x in lower:
        if not x.isalpha():
            continue
        elif x in char_freq:
            char_freq[x] += 1
        else:
            char_freq[x] = 1

    return char_freq
