import os
import sys


def input_files():
    arg = sys.argv[1]
    file_list = []
    if os.path.isfile(arg):
        file_list.append(arg)
    elif os.path.isdir(arg):
        for f in os.listdir(arg):
            file_list.append(f)
    else:
        raise FileNotFoundError("Input file does not exist")
    return file_list
