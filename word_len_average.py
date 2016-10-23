import shared
from operator import itemgetter
from collections import OrderedDict


TOTAL_WORDS = 100
ranking = {}  # {'lang': 3.42}

for lang in shared.input_files():
    total_len = 0.0
    frequency = shared.word_frequency(lang)
    for w in frequency.most_common(TOTAL_WORDS):
        total_len += len(w[0])
    ranking[lang] = total_len / TOTAL_WORDS

ranking_sorted = OrderedDict(sorted(ranking.items(), key=itemgetter(1), reverse=True))

for i in ranking_sorted.items():
    code = i[0].replace('all-langs/', '').replace('.txt', '')
    label = shared.langcode_label(code)
    if label == "Voynich": label = "##### Voynich #####"
    print("{:<19} {:.2f}".format(label, i[1]))
