from collections import Counter


def clear_punctuation(text):
    return ''.join([c.lower() for c in text if c.isalpha()])


def open_verse():
    with open('verse.txt', 'r', encoding='utf-8') as file_in:
        v = ''
        for line in file_in:
            v += line

        v = clear_punctuation(v)

    return v


def get_five(v):
    dct = Counter(v)
    five_tuples = dct.most_common(5)
    return [t[0] for t in five_tuples]
