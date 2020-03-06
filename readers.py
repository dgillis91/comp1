# Require compatibility for python 2. Pull commmon
# changes.
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)


DEFAULT_FILE_EXT = '.sp2020'


# In python3, raw_input is input
try:
    input = raw_input
except NameError:
    pass


class Reader:
    def read_text_as_list(self):
        raise NotImplementedError()


class FileReader(Reader):
    def __init__(self, filename):
        self._filename = filename + DEFAULT_FILE_EXT

    def read_text_as_list(self):
        with open(self._filename, 'r') as input_file:
            return list(input_file.read())

class KeyboardReader(Reader):
    def __init__(self):
        pass

    def read_text_as_list(self):
        tokens = list()
        while True:
            try:
                tokens.extend(list(input()))
            except EOFError:
                break

