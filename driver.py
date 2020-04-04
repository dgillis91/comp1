from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
import argparse
from fsa import initialize_scanner

parser = argparse.ArgumentParser()
parser.add_argument('path', help='path to file. do not include ext.')
args = parser.parse_args()


scanner = initialize_scanner(args.path)
for token in scanner.get_token():
    print(token)
