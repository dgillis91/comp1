# TODO: Need line number data back
# TODO: Need to filter out comments in the scanner class. 
# Require compatibility for python 2. Pull commmon
# changes.
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from readers import Reader


class Scanner:
    def __init__(self, reader: Reader):
        self._data = reader.read_text_as_list()

    def scan(self):
        for character in self._data:
            yield character
