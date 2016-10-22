import shared


for lang in shared.input_files():
    frequency = shared.word_frequency(lang)
    print(lang)
    for w in frequency.most_common(5):
        print(w)
    print()
