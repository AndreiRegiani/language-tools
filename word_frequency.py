import shared


LIMIT = 10

for lang in shared.input_files():
    frequency = shared.word_frequency(lang)
    print(lang, '\n')
    for w in frequency.most_common(LIMIT):
        print('  ', w[0])
    print()
