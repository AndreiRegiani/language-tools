import os
import sys
from collections import Counter
from langcodes import Language


IGNORE_CHARS = ".,:;/\“”‛’’‘″′″′‚—–-—=)(}{][?%><ӏӏ|·«»°•··،·፣፡¹‧।→%△►་◄%~′\'\"1234567890"


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
            if os.path.isfile(dir_file):
                file_list.append(dir_file)
    else:
        raise FileNotFoundError("File input does not exist")
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


def langcode_name(code):
    return Language.make(language=code).language_name().title()
