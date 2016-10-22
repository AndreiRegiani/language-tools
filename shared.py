import os
import sys
from collections import Counter


IGNORE_CHARS = ''


def input_files():
    try:
        arg = sys.argv[1]
    except IndexError:
        print("Usage: input_file_or_folder")
        sys.exit(1)

    file_list = []
    if os.path.isfile(arg):
        file_list.append(arg)
    elif os.path.isdir(arg):
        for file_ in os.listdir(arg):
            dir_file = "{}/{}".format(arg.replace('/', ''), file_)
            file_list.append(dir_file)
    else:
        raise FileNotFoundError("Input file does not exist")
    return file_list


def word_frequency(file_):
    wordlist = Counter()  # [('word', 1)]
    with open(file_) as fin:
        for line in fin:
            for char in IGNORE_CHARS:
                line = line.replace(char, ' ')
            words = line.lower().split()
            wordlist.update(words)
    return wordlist
