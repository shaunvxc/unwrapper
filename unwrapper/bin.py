from __future__ import print_function

import sys

from .application import unwrap


def main():
    if sys.stdin.isatty():
        result = unwrap(sys.argv[1])
    else:
        result = unwrap(sys.stdin.read())
    print(result)
