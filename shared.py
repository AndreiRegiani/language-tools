import os
import sys


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
        for f in os.listdir(arg):
            file_list.append(f)
    else:
        raise FileNotFoundError("Input file does not exist")
    return file_list
